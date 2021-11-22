import configparser  # import needed packages
import logging
import random
import mysql.connector


config = configparser.ConfigParser()
config.read('./config.ini')

mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')


number = random.randint(1, 15)

# logging setup
logging.basicConfig(filename='guess.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


#database connection
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db,
                                    user=mysql_config_mysql_user, password=mysql_config_mysql_pass)

mycursor = connection.cursor()

player_name = input("Hello, what is your name? ")
logging.info('****NEW GAME****')
logging.info('Player has to guess: ' + str(number))
logging.info('Player name ' + player_name)


number_of_guesses = 0
score = 0
print(
    'I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 15 then you will '
    'guess, alright? \nDon\'t forget! You have only 5 chances so guess:'.format(player_name))

# cycle for the guessees
while number_of_guesses < 5:
    guess = int(input())
    logging.info('Player guessed: ' + str(guess))
    number_of_guesses += 1
    if guess < number:
        print('Your estimate is too low, go up a little!')
    if guess > number:
        print('Your estimate is too high, go down a bit!')
    if guess == number:
        break
        # Game ending
if guess == number:
    score = 60/number_of_guesses
# Ievada rezultātu datubāze
    mycursor.execute(
        "INSERT INTO data (name,score,guesses) VALUES ('" + str(player_name) + "','"+ str(score) + "','"+ str(number_of_guesses) + "')")
    connection.commit()


    print('Congratulations {}, you guessed the number in {} tries! Your score is {}!'.format(player_name, number_of_guesses, score))
    logging.info('Player won with ' + str(number_of_guesses) + ' guesses. Score is ' + str(score))
else:
    score = 0
    print('Close but you couldn\'t guess the number. \nWell, the number was {}. Your score is {}'.format(number, score))
    logging.info('Player lost. Score is ' + str(score))
# Ievada rezultātu datubāze
    mycursor.execute(
        "INSERT INTO data (name,score,guesses) VALUES ('" + str(player_name) + "','" + str(score) + "','" + str(
            number_of_guesses) + "')")
    connection.commit()

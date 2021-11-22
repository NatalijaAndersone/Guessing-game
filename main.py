import configparser  # import needed packages
import logging
import random

config = configparser.ConfigParser()
config.read('./config.ini')

number = random.randint(1, 15)

# logging setup
logging.basicConfig(filename='guess.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

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
    print('Congratulations {}, you guessed the number in {} tries! Your score is {}!'.format(player_name, number_of_guesses, score))
    logging.info('Player won with ' + str(number_of_guesses) + ' guesses. Score is ' + str(score))
else:
    score = 0
    print('Close but you couldn\'t guess the number. \nWell, the number was {}. Your score is {}'.format(number, score))
    logging.info('Player lost. Score is ' + str(score))

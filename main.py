import random, logging
number = random.randint(1, 10)


logging.basicConfig(filename='guess.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


player_name = input("Hello, what is your name? ")
logging.info('****NEW GAME****')
logging.info('Player has to guess: ' + str(number))
logging.info('Player name ' + player_name)
number_of_guesses = 0
print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 10 then you will guess, alright? \nDon\'t forget! You have only 3 chances so guess:'.format(player_name))

while number_of_guesses < 3:
    guess = int(input())
    logging.info('Player guessed: ' + str(guess))
    number_of_guesses += 1
    if guess < number:
        print('Your estimate is too low, go up a little!')
    if guess > number:
        print('Your estimate is too high, go down a bit!')
    if guess == number:
        break
if guess == number:
    print( 'Congratulations {}, you guessed the number in {} tries!'.format(player_name, number_of_guesses))
    logging.info('Player won with ' + str(number_of_guesses) + ' number of guesses')
else:
    print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was {}.'.format(number))
    logging.info('Player lost')
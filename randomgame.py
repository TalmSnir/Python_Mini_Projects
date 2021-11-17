import random as rnd
import sys

first_num, second_num = sys.argv[1], sys.argv[2]
keep_playing = 'y'
while keep_playing == 'y':
    try:
        user_guess = input(
            "Please enter a number between {} to {}: ".format(first_num, second_num))
    except
    random_num = rnd.randint(int(first_num), int(second_num))
    print("the computer choose: {}".format(random_num))
    if int(user_guess) == random_num:
        print("you guessed correctly")
    else:
        print("maybe next time")


# !adding try and errors to the game

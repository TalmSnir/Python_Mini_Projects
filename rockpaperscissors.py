from random import choice

weapons_list = ["rock", "paper", "scissors"]

re_match = "y"
good_weapon = False
player_weapon = None

while re_match == "y":
    print("welcome to the rock,paper, scissors!")
    while good_weapon == False:
        player_weapon = input("what's your weapon of choice?")
        if player_weapon in weapons_list:
            good_weapon = True
        else:
            print("you should only choose from:rock,paper scissors")
    good_weapon = False
    computer_weapon = choice(weapons_list)
    print(" the computer choose: {} and you choose: {}".format(
        computer_weapon, player_weapon))

    if computer_weapon == player_weapon:
        print("its a tie, lets play again")
    elif computer_weapon == "rock":
        if player_weapon == "paper":
            print("you won")
        else:
            print("the computer has won")
    elif computer_weapon == "paper":
        if player_weapon == "scissors":
            print("you won")
        else:
            print("the computer has won")
    elif player_weapon != "paper":
        print("you won")
    else:
        print("the computer has won")
    re_match = input("do you want to play again? y/n ")

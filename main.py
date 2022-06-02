# Rock paper scissors game

import random

print("*****Welcome to Rock-Paper Scissors Game***** ")
print("***Rock beats Scissors")
print("***Paper beats Rock")
print("***Scissors beats Paper")
print("**'R' for 'Rock'**'P' for 'Paper'****'S' for 'Scissors'** ")
# list to contain available options
options = ["R", "P", "S"]

# randomizing options for computer's sake
computer_choice = random.choice(options)

# create loop
while True:
    # Accept user's option
    user_option = input("Pick an option from 'R', 'P', or 'S' :\n")
    # check if user's pick is in the list

    if user_option in options:
        print(f"Player:{user_option}, CPU {computer_choice}")
        # if the previous conditon was true, it proceeds to check if the user's option is equal to computer's random pick    if true, its a tie, user picks an option again

        if (user_option == computer_choice):
            print(f" it's a tie, pick an option again")

        # if user picks R and computer picks S, rock beats scissors, user wins, if not, computer wins. game ends

        elif (user_option == "R"):
            if(computer_choice == "S"):
                print("Rock beats Scissors, You Win!")
            else:
                print("Paper beats Rock, You lose!")
            break

        # if user picks P and computer picks R, paper beats rock, user wins, else computer wins. game ends
        elif (user_option == "P"):
            if (computer_choice == "R"):
                print("Paper beats Rock, You Win!")
            else:
                print("Scissors beat Paper, You loose!")
            break

        # if user picks S and computer picks S, Scissors beats paper, user wins, else computer wins. game ends
        elif (user_option == "S"):
            if(computer_choice == "P"):
                print("Scissors beats Paper, You Win!")
            else:
                print("Print Rock beats Scissors, You loose!")
            break

    # if user's input doesnt match the given options, there's an opportunity to try again, which returns the loop back to step 1
    else:
        print("Error: Try again")

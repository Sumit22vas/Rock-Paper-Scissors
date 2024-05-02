import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

welcome_message = """
    *******************************
    *                             *
    *           WELCOME           *
    *             TO              * 
    *    ROCK, PAPER, SCISSORS    *
    *                             *
    *******************************
    
    """
print(welcome_message)

def play_rps_game():



    # Collect Player Input
    player_choice = input(
        "\nEnter... \n 1 for ROCK \n 2 for PAPER \n 3 for SCISSORS\n\n")

    # Make Sure input is 1,2 or 3
    if player_choice not in ["1","2","3"]:
        print("Wrong Option Selected 👎")
        return play_rps_game() # recurssive call
        
    # casting Player input in integer
    player = int(player_choice)

    # generate a random computer number for computer
    computer_choice = random.choice("123")

    # cast computer_choice to integer
    computer = int(computer_choice)

    print("\nYou Chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Computer Chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    # game logic
    if player == 1 and computer == 3:
        print("You Win! 🎉🎉🎉")
    elif player == 2 and computer == 1:
        print("You Win! 🎉🎉🎉")
    elif player == 3 and computer == 2:
        print("You Win! 🎉🎉🎉")
    elif player == computer:
        print("It's a tie. 😃")
    else:
        print("💻 Computer wins!")

    
    # ask player if they want to play again or quit
    while True:
        play_again = str(input("\n\n Do you want to play again ? Enter...\n Y to play again\n Q to quit the game\n"))
        if play_again.lower() not in ['y','q']:
            continue
        else:
            break

    if play_again.lower() == 'y':
        play_rps_game() 
    else:
        print("\n Thanks for playing... .🙏")
        print("Bye Bye! 👋👋👋")
        
    
play_rps_game()
    
    

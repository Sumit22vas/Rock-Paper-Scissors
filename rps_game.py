import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


play_game_again = True

while play_game_again:

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

    # Collect Player Input
    player_choice = input(
        "\nEnter... \n 1 for ROCK \n 2 for PAPER \n 3 for SCISSORS\n\n")

    # casting Player input in integer
    player = int(player_choice)

    # Make sure player provides a number which is not lesser than 1 or greater than 3
    if player < 1 or player > 3:
        sys.exit("Please enter 1, 2 or 3\n")

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

    play_again = str(input("\n\n Do you want to play again ? Enter...\n Y to play again\n Q to quit the game\n"))

    if play_again.lower() == 'y':
        play_game_again = True
        continue
    else:
        play_game_again = False
    
else: # termination of while loop
    print("\n Bye Bye! 👋👋🙋👋")
    

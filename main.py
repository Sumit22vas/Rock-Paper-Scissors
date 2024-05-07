import argparse
from rps_game import play_game,print_welcome_msg
# create a argument parser
parser = argparse.ArgumentParser(description="Helps in using player name in the game")

parser.add_argument("-n","--name",help="Stores player name",dest="player_name",required=True)
# parsing arguments from command line
args = parser.parse_args()

if __name__ == "__main__":
    # print welcome message
    print_welcome_msg(args.player_name)
    # start the game with play name
    play_game(args.player_name)
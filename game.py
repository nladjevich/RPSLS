from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.round = 0
        self.players = 0

    def welcome(self):
        print("Welcome to Rock, Paper, Scissor, Spock!!\n\nEach of the games will be best out of three.\nUse the numbers keys to enter in your inputs.\n Here are the rules.\nRock crushes Scissors\n\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")

    def choose_players(self):
        players = int(input("How many players will be playing? 1 or 2?"))
        if players != 1 or 2:
            print("Please select 1 or 2 players.")
            Game.choose_players(self)
        self.players = players

    def one_player_game():
        print(f"{Human.name} will be going first. Make your selection.")
        Human.choose_gesture
        Ai.random_choice


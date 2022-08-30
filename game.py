from human import Human
from ai import Ai
from player import Player
from human_2 import Human2
class Game(Player):
    def __init__(self):
        super().__init__()
        self.round = 0
        self.players = 0

    def welcome(self):
        print("Welcome to Rock, Paper, Scissor, Spock!!\n\nEach of the games will be best out of three.\nUse the numbers keys to enter in your inputs.\n Here are the rules.\nRock crushes Scissors\n\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")

    def choose_players(self):
        players = int(input("How many players will be playing? 1 or 2?"))
        if players == 1:
            print("You will be playing with an Ai.")
        elif players == 2:
            print("You will be playing with another person.")
        else:
            print("Please enter 1 or 2.")
            Game.choose_players(self)
        self.players = players

    def one_player_game(self):
        print(f"Human will be going first. Make your selection.")
        while self.round < 3:
            human_choice = Human.choose_gesture(self)
            ai_choice = Ai.random_choice(self)
            human_win = False
            ai_win = False
            if human_choice == ai_choice:
                print("It was a tie.")
            elif human_choice == "Rock":
                if ai_choice == "Paper":
                    print("Ai wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif ai_choice == "Scissor":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Lizard":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Spock":
                    print("Ai wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_choice == "Paper":
                if ai_choice == "Scissor":
                    print("Ai wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif ai_choice == "Rock":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Spock":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Lizard":
                    print("Ai wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_choice == "Scissor":
                if ai_choice == "Rock":
                    print("Ai wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif ai_choice == "Paper":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Lizard":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Spock":
                    print("Ai wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_choice == "Lizard":
                if ai_choice == "Rock":
                    print("Ai wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif ai_choice == "Spock":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Paper":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Scissor":
                    print("Ai wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_choice == "Spock":
                if ai_choice == "Lizard":
                    print("Ai wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif ai_choice == "Scissor":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Rock":
                    print("Human wins, round over")
                    self.round += 1
                    human_win += 1
                elif ai_choice == "Paper":
                    print("Ai wins, round over")
                    self.round += 1
                    ai_win += 1
        if human_win > ai_win:
            print("Human wins!! Game over.")
        elif ai_win > human_win:
            print("Ai wins!! Game over.")

    def two_player_game(self):
        print("Human 1 will go first. Make your selection.")
        while self.round < 3:
            human_1_choice = Human.choose_gesture(self)
            human_2_choice = Human2.choose_gesture(self)
            human_win = False
            ai_win = False
            if human_1_choice == human_2_choice:
                print("It was a tie.")
            elif human_1_choice == "Rock":
                if human_2_choice == "Paper":
                    print("Human 2 wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif human_2_choice == "Scissor":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Lizard":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Spock":
                    print("Human 2 wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_1_choice == "Paper":
                if human_2_choice == "Scissor":
                    print("Human 2 wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif human_2_choice == "Rock":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Spock":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Lizard":
                    print("Human 2 wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_1_choice == "Scissor":
                if human_2_choice == "Rock":
                    print("Human 2 wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif human_2_choice == "Paper":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Lizard":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Spock":
                    print("Human 2 wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_1_choice == "Lizard":
                if human_2_choice == "Rock":
                    print("Human 2 wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif human_2_choice == "Spock":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Paper":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Scissor":
                    print("Human 2 wins, round over")
                    self.round += 1
                    ai_win += 1
            elif human_1_choice == "Spock":
                if human_2_choice == "Lizard":
                    print("Human 2 wins, round is over!")
                    self.round += 1
                    ai_win += 1
                elif human_2_choice == "Scissor":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Rock":
                    print("Human 1 wins, round over")
                    self.round += 1
                    human_win += 1
                elif human_2_choice == "Paper":
                    print("Human 2 wins, round over")
                    self.round += 1
                    ai_win += 1
        if human_win > ai_win:
            print("Human 1 wins!! Game over.")
        elif ai_win > human_win:
            print("Human 2 wins!! Game over.")



                
            




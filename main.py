from player import Player
from ai import Ai
from human import Human
from game import Game

ai_1 = Ai()
human_1 = Human("John")
game_1 = Game()

game_1.welcome()
game_1.choose_players()
if game_1.players == 1:
    game_1.one_player_game()
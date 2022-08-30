
from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.name = "Ai"
        

    def random_choice(self):
        ai_choice = random.choice(self.gesture_list)
        self.chosen_gesture = ai_choice
        print(f"Ai has chosen {self.chosen_gesture}!")
        return ai_choice



        
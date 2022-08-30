from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        human_choice = int(input("Pick 0 for Rock.\nPick 1 for Paper.\nPick 2 for Scissor.\nPick 3 for Lizard.\nPick 4 for Spock."))
        if human_choice == 0:
            self.chosen_gesture = "Rock"
        elif human_choice == 1:
            self.chosen_gesture = "Paper"
        elif human_choice == 2:
            self.chosen_gesture = "Scissor"
        elif human_choice == 3:
            self.chosen_gesture = "Lizard"
        elif human c
        return human_choice




        
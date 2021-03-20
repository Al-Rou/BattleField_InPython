from player import player
import random

#One player is called monster, which is in fact the computer
class Monster(player):
    def __init__(self, life):
        super().__init__(life)

    # This method determines how much damage will be imposed from Monster to Human
    def damage(self):
        d = random.randint(3, 14)
        return d

    # This method outputs the state of Monster at each stage
    def printData(self):
        print(self.life, self.loseStatus)
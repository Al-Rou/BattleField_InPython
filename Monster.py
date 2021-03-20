from player import player
import random

class Monster(player):
    def __init__(self, life):
        super().__init__(life)

    def damage(self):
        d = random.randint(3, 14)
        return d

    def printData(self):
        print(self.life, self.loseStatus)
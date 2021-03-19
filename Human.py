from enum import Enum
from player import player
import random

class Human(player):
    def __init__(self, life, mana):
        super().__init__(life)
        self.mana = mana
    #Weapon = Enum('Weapon', 'sword fireball')
    def setWeapon(self, w):
        self.choiceOfWeapon = w

    def printData(self):
        print(self.life, self.mana, self.choiceOfWeapon)

    def damage(self):
        if self.choiceOfWeapon == "Sword":
            d = random.randint(7, 9)
            return d
        elif self.choiceOfWeapon == "Fireball":
            if self.mana > 9:
                d = random.randint(1, 18)
                self.mana -= 10
                return d
            else:
                print("You don't have enough mana to employ Fireballs!")

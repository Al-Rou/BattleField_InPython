from player import player
import random

#One player is called human, who is in fact the user
class Human(player):
    def __init__(self, life, mana):
        super().__init__(life)
        self.mana = mana

    #The chosen weapon is set here
    def setWeapon(self, w):
        self.choiceOfWeapon = w

    #This method outputs the state of Human at each stage
    def printData(self):
        print(self.life, self.mana, self.choiceOfWeapon, self.loseStatus)

    #This method determines how much damage will be imposed from Human to Monster
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
                d = random.randint(7, 9)
                return d

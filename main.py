from enum import Enum
#import Human
from player import player
from Human import Human
import random

h = Human(100, 35)
w = input("What weapon (Sword or Fireball)?")
h.setWeapon(w)
h.printData()
d = h.damage()
print(d)
h.printData()
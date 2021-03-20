from player import player
from Human import Human
from Monster import Monster

class goPlaying:
    def __init__(self):
        h = Human(100, 35)
        m = Monster(100)
        while((h.life > 0) and (m.life > 0)):
            w = input("Choose your weapon (Sword or Fireball):")
            h.setWeapon(w)
            m.life -= h.damage()
            m.printData()
            h.life -= m.damage()
            h.printData()
        if h.life <= 0:
            h.loseStatus = True
            h.printData()
            print("Monster won!")
            m.printData()
        else:
            m.loseStatus = True
            m.printData()
            print("Human won!")
            h.printData()
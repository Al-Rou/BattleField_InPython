from player import player
from Human import Human
from Monster import Monster

#This class defines how the play should go on
#As soon as this class is instantiated, the play starts
class goPlaying:
    def __init__(self):
        h = Human(100, 35)
        m = Monster(100)
        while((h.life > 0) and (m.life > 0)):
            w = input("Choose your weapon (Sword or Fireball):")
            while (w != "Sword") and (w != "Fireball"):
                print("Your choice of weapon is not valid!")
                w = input("Choose your weapon (Sword or Fireball):")
            h.setWeapon(w)
            m.life -= h.damage()
            m.printData()
            h.life -= m.damage()
            h.printData()
        if h.life <= 0:
            h.loseStatus = True
            print("Human lost with below results:")
            h.printData()
            print("Monster won!")
            m.printData()
        else:
            m.loseStatus = True
            print("Monster lost with below results:")
            m.printData()
            print("Human won!")
            h.printData()
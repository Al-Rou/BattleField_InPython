#This class is a parent class for both players
class player:
    def __init__(self, life):
        self.life = life
        self.loseStatus = False

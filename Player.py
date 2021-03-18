class Player:
    def __init__(self, life):
        self.life = life
        self.loseStatus = False

    def getLoseStatus(self):
        return self.loseStatus
    def setLoseStatus(self, newStatus):
        self.loseStatus = newStatus
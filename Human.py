class Human(Player):
    def __init__(self, life, mana):
        super().__init__(life)
        self.mana = mana
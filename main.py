from enum import Enum

class dirst:
    def first(self):
        for i in range (10):
            i += 2
            print(i)

    Weapon = Enum('Weapon', 'sword fireball')

a = dirst()
a.first()
print(a.Weapon.fireball.name)
print(a.Weapon.fireball)
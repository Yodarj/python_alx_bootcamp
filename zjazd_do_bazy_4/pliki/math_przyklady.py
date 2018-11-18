import math

print(math.sin(math.pi/2))

print(math.tau)

'''
Stwórz klasę sfera

s = Sfera(10)
s.promien # 10

objetnosc
pole_powierzchni
'''

class Sfera:
    def __init__(self, r):
        self.promien = r

    def promien(self):
        return self.promien

    def objetosc(self):
        return 4/3*math.pi*self.promien**3

    def pole_powierzchni(self):
        return 4*math.pi*self.promien**2


s = Sfera(10)

print(s.promien)
print(s.objetosc())
print(s.pole_powierzchni())






# ----- wprowadzenie

x = 1
napis = 'napis'
y = 1.2
slownik = {}


def foo():
    pass


print(type(x), type(napis), type(y), type(slownik), type(foo))

#definicja klasy
class Animal:
    nazwa = "Fauna" # atrybut CAŁEJ klasy
    licznik = 0

    def __init__(self, gatunek):
        self.gatunek = gatunek # atrybut instancji, obiektu
        self.zwieksz_licznik()
        self.stan = "Bierny"

    def __str__(self):
        return "Animal"

    def idz(self):
        self.stan = "Idzie"

    def stoj(self):
        self.stan = "Stoi"

    def spij(self):
        self.stan = "Śpi"

    @classmethod
    def zwieksz_licznik(cls):
        cls.licznik += 1

class LeniweZwierzeta(Animal):

    def idz(self):
        self.stan = "Leży"
        print("Chyba śnisz")

#tworzenie instancji klasy
azor = Animal("Canis Lupus")
rudolf = Animal("Rangifer tarandus")

print(azor)
print(azor.gatunek)
print(rudolf.gatunek)

print(Animal.licznik)

azor.idz()
print(azor.stan)
garfield = LeniweZwierzeta("Felis Catus")

#garfield.idz()
LeniweZwierzeta.idz(garfield)

print(garfield.stan)

garfield.spij()

print(garfield.stan)
print(azor.stan)

#dziedziczenie

class LeniweZwierzeta(Animal):
    pass


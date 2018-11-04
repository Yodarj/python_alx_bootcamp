# Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
# swobodnego na dwuwymiarowej płaszczyźnie. Wektory powinny
# mieć możliwość dodawania, odejmowania, mnożenia (przez inny
# wektor i przez liczbę), porównywania (po długości) oraz powinny
# posiadać czytelną reprezentację napisową.
# Przykład użycia:
# vector_1 = Vector(x=1, y=2)
# vector_2 = Vector(x=1, y=2)
# vector_3 = vector_1 + vector_2

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, second_vector):
        return Vector(self.x + second_vector.x, self.y + second_vector.y)

    def __sub__(self, second_vector):
        return Vector(self.x - second_vector.x, self.y - second_vector.y)

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number)

    def dlugosc(self):
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5

    def __eq__(self, second_vector):
        return self.x == second_vector.x and self.y == second_vector.y

    def __lt__(self, second_vector):
        return self.dlugosc() < second_vector.dlugosc()

    def __gt__(self, second_vector):
        return self.dlugosc() > second_vector.dlugosc()


def test_vector_all_fun():
    vector_1 = Vector(x=-1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 0
    assert vector_3.y == 4
    vector_4 = vector_1 - vector_2
    assert vector_4.x == -2
    assert vector_4.y == 0
    vector_5 = vector_1 * 2
    assert vector_5.x == -2
    assert vector_5.y == 4
    assert vector_1.dlugosc() == vector_2.dlugosc()
    assert vector_1 != vector_2
    assert vector_2 < vector_3
    assert vector_5 > vector_3
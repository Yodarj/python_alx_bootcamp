"""
Stwórz klasę Dog wedgług następującej specyfikacji:

•pies zużywa energię szczekając (bark) i zyskuje śpiąc (sleep).
•nowa instancja klasy Dog ma 10 jednostek energii
•Dog ma metodę sleep która dodaje mu 2 jednostki energii
•Dog ma metodę bark która konsumuje mu 1 jednostkę energii
•Dog ma metodę get_energy która zwraca wartość energii instancji

"""


class Dog:

    def __init__(self):
        self.energia = 10

    def sleep(self):
        self.energia += 2

    def bark(self):
        self.energia -= 1

    def get_energy(self):
        return self.energia

def test_dog():
    pies = Dog()

    print(pies.get_energy())
    assert pies.get_energy() == 10
    pies.bark()
    pies.bark()
    pies.bark()
    pies.sleep()

    assert pies.get_energy() == 9

class Product:

    def __init__(self, ID, nazwa, cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        return f'Produkt {self.nazwa}, id: {self.ID}, cena: {self.cena} PLN'


def test_product():

    product = Product(1, "Woda", 10.99)

    assert hasattr(product, "ID")
    assert hasattr(product, "cena")
    assert hasattr(product, "nazwa")

    assert product.ID == 1
    assert product.nazwa == "Woda"
    assert product.cena == 10.99


def test_woda_calosc():

     product = Product(1, "Woda", 10.99)

     assert product.print_info() == 'Produkt Woda, id: 1, cena: 10.99 PLN'
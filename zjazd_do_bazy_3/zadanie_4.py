class Product:

    def __init__(self, ID, nazwa, cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        return f'Produkt {self.nazwa}, id: {self.ID}, cena: {self.cena} PLN'


class Basket:

    def __init__(self):
        self.basket = {}

    def add_product(self, product, ilosc):
        self.product = product
        self.ilosc = ilosc
        self.basket.update({product.nazwa:product.cena})

    def count_total_price(self):
        cena = self.ilosc * self.product.cena
        return cena

    def generate_report(self):
        return f'''Produkty w koszyku:\n 
    - {self.product.nazwa} ({self.product.ID}), cena: {self.product.cena} x {self.ilosc}\n
    W sumie: {self.count_total_price()}'''

basket = Basket()
product = Product(1, "Woda", 10.99)
basket.add_product(product, 5)

print(basket.product.cena)


def test_basket():
    basket = Basket()
    product = Product(1, "Woda", 10)
    basket.add_product(product, 5)

    assert basket.count_total_price() == 50.00

    assert basket.generate_report() == '''Produkty w koszyku:\n 
    - Woda (1), cena: 10 x 5\n
    W sumie: 50'''

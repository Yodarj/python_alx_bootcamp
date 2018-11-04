class Product:

    id = 1

    def __init__(self, name, price):
        self.id = Product.id
        Product.id += 1
        self.name = name
        self.price = price

    def print_info(self):
        return f'Produkt {self.name}, id: {self.id}, cena: {self.price} PLN'

class BasketEntry:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity

class Basket:

    def __init__(self):
        self.entries = []
        self.product = None
        self.quantity = None

    def __str__(self):
        return "Basket"

    def add_product(self, product, quantity):
        basket_entry = BasketEntry(product, quantity)
        self.entries.append(basket_entry)

    def count_total_price(self):
        amount = 0
        for entry in self.entries:
            amount += entry.count_price()
        return amount

    def generate_report(self):
        text_1 = f'''Produkty w koszyku:\n'''
        text_2 = str()
        for entry in self.entries:
            text_2 += f'''- {entry.product.name} ({entry.product.id}), cena: {entry.product.price} x {entry.quantity}\n'''
        text_3 = f'''W sumie: {self.count_total_price()}'''
        return text_1 + text_2 + text_3


def test_create_basket():
    basket = Basket()
    assert str(basket) == "Basket"
    assert basket.entries == []


def test_add_product_to_basket():
    basket = Basket()
    product = Product("Woda", 10)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1

def test_basket_count_total_price():
    basket = Basket()
    product = Product("Woda", 10)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50.0

def test_add_product_to_basket_x2():
    basket = Basket()
    product_1 = Product("Woda", 10)
    product_2 = Product("Wóda", 15)
    basket.add_product(product_1, 5)
    basket.add_product(product_2, 10)
    assert len(basket.entries) == 2

def test_basket_count_total_price_2():
    basket = Basket()
    product_1 = Product("Woda", 10)
    product_2 = Product("Wóda", 15)
    basket.add_product(product_1, 5)
    basket.add_product(product_2, 10)
    assert basket.count_total_price() == 200.0

def test_basket_generate_report():
    basket = Basket()
    product = Product("Woda", 10)
    basket.add_product(product, 5)
    assert basket.generate_report() == '''Produkty w koszyku:
- Woda (1), cena: 10 x 5
W sumie: 50'''

def test_basket_generate_report_more():
    basket = Basket()
    product_1 = Product("Woda", 10)
    product_2 = Product("Wóda", 15)
    basket.add_product(product_1, 5)
    basket.add_product(product_2, 10)
    assert basket.generate_report() == '''Produkty w koszyku:
- Woda (1), cena: 10 x 5
- Wóda (2), cena: 15 x 10
W sumie: 200'''

class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.godziny = 0

    def register_time(self, godziny):
        self.godziny += godziny

    def pay_salary(self):
        h_pracy = self.godziny
        if self.godziny <= 8 and self.godziny > 0:
            self.godziny = 0
            salary = h_pracy * self.stawka
            return salary
        elif self.godziny > 8:
            self.godziny = 0
            salary = (8 * self.stawka) + ((h_pracy - 8) * 2 * self.stawka)
            return salary
        else:
            self.godziny = 0
            return 0

class PremiumEmployee(Employee):

    def give_bonus(self, bonus):
        self.bonus = bonus

    def pay_salary(self):
        h_pracy = self.godziny
        if self.godziny <= 8 and self.godziny > 0:
            self.godziny = 0
            salary = h_pracy * self.stawka + self.bonus
            return salary
        elif self.godziny > 8:
            self.godziny = 0
            salary = (8 * self.stawka) + ((h_pracy - 8) * 2 * self.stawka) + self.bonus
            return salary
        else:
            self.godziny = 0
            return 0


def test_premium():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000.0)
    assert employee.pay_salary() == 1500.0
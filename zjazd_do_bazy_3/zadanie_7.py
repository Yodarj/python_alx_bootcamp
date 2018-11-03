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

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus = bonus

    def pay_salary(self):
        to_pay = super().pay_salary()
        return to_pay + self.bonus


# utwórz klasę Company, którą inicjalizuję się z nazwą
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> google = Company('Google')
# >>> google.add_employee(employee)
# >>> google.size()
# 1
# >>> google.pay_all_salary()
# 500
# >>> google.pay_all_salary()
# 0
# >>> employee2 = Employee('Krzysztof', 'Nowak', 200.0)
# >>> employee2.register_time(5)
# >>> google.add_employee(employee2)
# >>> google.pay_all_salary()
# 1000

class Company:

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.salary = 0
        self.size = 0
        self.emp_list = []
        self.salary = 0

    def add_employee(self, employee):
        self.employee = employee
        self.size += 1
        self.emp_list.append(employee)
        self.salary += self.employee.pay_salary()


    def size(self):
        return self.size

    def pay_all_salary(self):
        all_salary = self.salary
        self.salary = 0
        return all_salary


def test_company_size():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    google = Company('Google')
    google.add_employee(employee)
    assert google.size == 1


def test_company_salary():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    google = Company('Google')
    google.add_employee(employee)
    assert google.pay_all_salary() == 500.0
    assert google.pay_all_salary() == 0


def test_company_salary2():
    employee2 = Employee('Krzysztof', 'Nowak', 200.0)
    employee2.register_time(5)
    google = Company('Google')
    google.add_employee(employee2)
    assert google.pay_all_salary() == 1000.0
    assert google.pay_all_salary() == 0


def test_company_salary3():
    employee3 = Employee('Krzysztof', 'Nowak', 300.0)
    employee4 = Employee('Krzysztof', 'Nowak', 400.0)
    employee3.register_time(5)
    employee4.register_time(5)
    google = Company('Google')
    google.add_employee(employee3)
    google.add_employee(employee4)
    assert google.size == 2
    assert google.pay_all_salary() == 3500.0
    assert google.pay_all_salary() == 0

def test_company_salary4():
    employee5 = Employee('Krzysztof', 'Nowak', 300.0)
    employee6 = Employee('Andrzej', 'Nowak', 400.0)
    employee7 = Employee('Dobromir', 'Nowak', 200.0)
    employee5.register_time(5)
    employee6.register_time(10)
    employee7.register_time(20)
    google = Company('Google')
    google.add_employee(employee5)
    google.add_employee(employee6)
    google.add_employee(employee7)
    assert google.size == 3
    assert google.pay_all_salary() == 1500 + 3200 + 1600 + 1600 + 4800
    assert google.pay_all_salary() == 0

def test_premium():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000.0)
    assert employee.pay_salary() == 1500.0

class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.godziny = 0

    def register_time(self, godziny):
        self.godziny = godziny

    def pay_salary(self):
        if self.godziny <= 8:
            return self.godziny * self.stawka
        else:
            return (8 * self.stawka) + ((self.godziny-8)*2*self.stawka)





def test_employee_5h():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500.0

def test_employee_0h():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0

def test_employee_10h():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200.0
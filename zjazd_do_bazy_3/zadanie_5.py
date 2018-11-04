class CashMachine:
    def __init__(self):
        self.__cash = []
        self.money = []
        self.get_cash = 0

    @property
    def is_available(self):
        return len(self.__cash) > 0

    def put_money(self, money):
        self.money = money
        self.__cash.extend(money)

    def withdraw_money(self, get_cash):
        self.get_cash = get_cash
        cash_taken = []
        total_get = 0
        while total_get < get_cash:
            if not self.__cash:
                break
            else:
                min_account = min(self.__cash)
                total_get += min_account
                cash_taken.insert(0, min_account)
                self.__cash.remove(min_account)
        return cash_taken


def test_cash_machine_avail():
    cash_machine = CashMachine()
    assert cash_machine.is_available == False


def test_cash_machine_putting():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available == True


def test_cash_machine_withdraw():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]


def test_cash_machine_withdraw_2():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 10, 50])
    cash_machine.put_money([20, 100, 100, 50])
    cash_machine.put_money([200, 100, 50])
    cash_machine.put_money([200, 100])
    assert cash_machine.withdraw_money(180) == [50, 50, 50, 20, 10]
    assert cash_machine.withdraw_money(200) == [100, 100]
    assert cash_machine.withdraw_money(500) == [200, 100, 100, 100]
    assert cash_machine.is_available == True
    assert cash_machine.withdraw_money(500) == [200, 200]
    assert cash_machine.is_available == False

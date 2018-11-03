# ----- poniższa klasa z jupytera

class Kalkulator:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def policz_potege(self):
        return self.var1 ** self.var2

    def policz_sume(self, var3):
        return self.var1 + self.var2 + var3

calc = Kalkulator(2, 3)
assert calc.policz_potege() == 8
assert calc.policz_sume(4) == 9

print(calc.policz_potege())
print(calc.policz_sume(4))

# -------- yay!
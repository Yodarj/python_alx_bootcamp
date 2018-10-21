# Napisz program "prk.py", który obliczy wszystkie pierwiastki rzeczywiste równania kwadratowego o postaci ax^2+bx+c=0,
# gdzie a, b i c podaje użytkownik. Program powinien na początku sprawdzić,
# czy wprowadzone równanie jest rzeczywiście kwadratowe.

from math import sqrt

def prk(a, b, c):
    delta = b ** 2 - 4 * a * c
    if a == 0:
        print("No chyba nie ....")
        quit()
    if delta < 0:
        print("To równanie nie ma rozwiązania!!")
    elif delta == 0:
        x = (-b) / 2
        a
        print(f'Rozwiązaniem równania jest {x}')
    else:
        x_1 = ((-b) - sqrt(delta)) / (2 * a)
        x_2 = ((-b) + sqrt(delta)) / (2 * a)
        print(f'Rozwiązaniem równania są dwie wartości: {x_1} oraz {x_2}')


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

prk(a, b, c)

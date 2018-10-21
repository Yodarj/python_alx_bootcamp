import pytest


# def przywitaj_sie(x, y, z, c):
#     print('Cześć', x, y, z, c)
#
# lista_osob = [
#     {
#         'x': "Exo",
#         'y': "kuku",
#         'z': "bebe",
#         'c': "asd"
#     }
# ]
#
# for osoba in lista_osob:
#     przywitaj_sie(osoba['x'], osoba['y'], osoba['z'], osoba['c'])


# def czy_wieksza_niz_3(x):
#     if x > 3:
#         return True
#     return False
#
#
# def test_wieksza_niz_3_dla_wiekszej_niz_3():
#     assert True == czy_wieksza_niz_3(4)
#
#
# def test_wieksza_niz_3_dla_mniejszej_niz_3():
#     assert False == czy_wieksza_niz_3(2)
#
#
# def drukuj_linie():
#     print("-" * 40)
#
#
# drukuj_linie()
#
#
# def zwroc_wartosc_wpisana():
#     wartosc = input('Podaj coś! ')
#     return wartosc
#
#
# def sumator(a, b):
#     return a + b
#
#
# def tabliczka_mnozenia():
#     a = int(input('Podaj wartość a: '))
#     b = int(input('Podaj wartość b: '))
#     print(a * b)
#
#
# tabliczka_mnozenia()

def kalkulator(a, b, operacja='+', opis=''):
    if opis:
        print(opis)
    if operacja == '+':
        return a + b
    elif operacja == '-':
        return a - b


print(kalkulator(2, 1, '-', "daioshdiuahwiufhauiwd"))

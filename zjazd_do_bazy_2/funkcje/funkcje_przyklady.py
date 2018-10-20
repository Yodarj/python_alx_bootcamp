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


def czy_wieksza_niz_3(x):
    if x > 3:
        return True
    return False

def test_wieksza_niz_3_dla_wiekszej_niz_3():
    assert True == czy_wieksza_niz_3(4)

def test_wieksza_niz_3_dla_mniejszej_niz_3():
    assert False == czy_wieksza_niz_3(2)
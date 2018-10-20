#### moje poniżej poprawne!

# def wiecej_niz(napis, x):
#     napis.lower()
#     licznik = {}
#     zbior = set()
#     for litera in napis:
#         licznik[litera] = licznik.get(litera, 0) + 1
#     for i in licznik:
#         y = licznik[i]
#         if y > x:
#             zbior.add(i)
#         else:
#             continue
#     return zbior
#
# def test_wiecej_niz_dla_pustego_napisu():
#     assert wiecej_niz('',0) == set()
#
# def test_wiecej_niz_dla_niepustego_napisu():
#     assert wiecej_niz('aaaaaaabbccccccd', 2) == {'a', 'c'}
#
# print(wiecej_niz('asdawgawda',3))

# ------------------------------------------------------

def wiecej_niz(napis, z):
    licznik = {}
    wynik = set()
    for litera in napis:
        litera = litera.lower()
        licznik[litera] = licznik.get(litera, 0) + 1
    for key, value in licznik.items():
        if value > z:
            wynik.add(key)
    return wynik

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('',0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaaaabbccccccd', 2) == {'a', 'c'}

def test_wiecej_niz_dla_male_duze_litery():
    assert wiecej_niz('aaaAAAbbccccd', 5) == {'a'}

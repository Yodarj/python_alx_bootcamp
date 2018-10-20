def wiecej_niz(napis, x):
    napis.lower()
    licznik = {}
    zbior = set()
    for litera in napis:
        licznik[litera] = licznik.get(litera, 0) + 1
    for i in licznik:
        y = licznik[i]
        if y > x:
            zbior.add(i)
        else:
            continue
    return zbior

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('',0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaaaabbccccccd', 2) == {'a', 'c'}


wiecej_niz('aaabbbcccmmmnnnsdoa', 2)
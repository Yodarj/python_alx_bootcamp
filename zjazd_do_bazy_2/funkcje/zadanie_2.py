def wiecej_niz(napis):
    napis.lower()
    licznik = set()
    for litera in napis:
        if litera in licznik:
            licznik[litera] = licznik[litera] + 1
        else:
            licznik[litera] = 1



def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('',0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaaaabbccccccd', 2) == {'a', 'c'}



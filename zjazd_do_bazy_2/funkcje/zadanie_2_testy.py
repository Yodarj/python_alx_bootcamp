from zadanie_2 import wiecej_niz

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('',0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaaaabbccccccd', 2) == {'a', 'c'}

def test_wiecej_niz_dla_male_duze_litery():
    assert wiecej_niz('aaaAAAbbccccd', 5) == {'a'}
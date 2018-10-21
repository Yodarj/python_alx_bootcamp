def policz_znaki(napis='', znakod='<', znakdo='>'):
    mnoznik = 0
    licz = 0
    for znak in napis:
        if znak == znakod:
            mnoznik +=1
        elif znak == znakdo:
            mnoznik -= 1
        else:
            licz = licz + mnoznik
        #print(znak,licz, mnoznik)
    return licz


def test_policz_znaki_0():
    assert policz_znaki('') == 0
def test_policz_znaki_1():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
def test_policz_znaki_2():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
def test_policz_znaki_3():
    assert policz_znaki('a <a<a<a>>>') == 6

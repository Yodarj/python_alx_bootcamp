def test_funkcja_zliczajaca_1():
    assert funkcja_zliczajaca('ala ma <kota> a kot ma ale') == 4


def test_funkcja_zliczajaca_2():
    assert funkcja_zliczajaca('ala [kota [a kot]] ma [ale]', '[', ']') == 18


def test_funkcja_zliczajaca_3():
    assert funkcja_zliczajaca('a <a<a<a>>>') == 6


def funkcja_zliczajaca(napis='', znak_l='<', znak_p='>'):
    licznik = 0
    for litera in napis:
        if litera == znak_l:
            napis = napis[napis.index(litera):]
            for litera_wew in napis:
                if litera_wew == znak_l:
                    napis = napis[napis.index(litera_wew):]
                    for litera_wew_2 in napis:
                        if litera_wew_2 == znak_l:
                            napis = napis[napis.index(litera_wew_2):]
                            for litera_wew_3 in napis:
                                if litera_wew_3 == znak_p:
                                    break
                                licznik += 3
                        elif litera_wew_2 == znak_p:
                            break
                    licznik += 2
                elif litera_wew == znak_p:
                    break
            licznik += 1
        elif litera == znak_p:
            break
    return licznik

    # znak_1 = napis.find(znak_l)
    # znak_2 = napis.find(znak_p)
    # napisn = napis[znak_1 + 1:znak_2]
    # return len(napisn)


print(funkcja_zliczajaca("Coś nie tak [zi[om]ek] ?", '[', ']'))


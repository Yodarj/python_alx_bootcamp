def cenonator(cena, *args):
    zmiana = ''
    for x in args:
        x = (x.replace('$cena', f'{cena}'))
        if x == len(args):
            zmiana += x
        else:
            zmiana += x +'\n'
    return zmiana


# x = ['wódka $cena PLN', 'szmatka $cena PLN', 'głupota $cena PLN', 'tupet $cena PLN']
#
# cenonator(*x, cena=20)

def test_cenonator():
    assert cenonator(
        10,
        'koszt $cena PLN',
        'kwota $cena PLN brutto'
        ) == 'koszt 10 PLN\nkwota 10 PLN brutto'

print(cenonator(
        10,
        'koszt $cena PLN',
        'kwota $cena PLN brutto'))
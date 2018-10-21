def cenonator(*args, **kwargs):
    zmiana = []
    for x in args:
        for k in kwargs:
            x = x.replace(f'${k}', str(kwargs[k]))
        zmiana.append(x)
    return "\n".join(zmiana)


def test_cenonator_1():
    assert cenonator(
        'koszt $cena PLN',
        'kwota $cena PLN brutto',
        'sumarycznie &cena',
        'podatek: $podatek',
        cena=10,
        podatek=0.23
    ) == 'koszt 10 PLN\nkwota 10 PLN brutto\nsumarycznie 10\npodatek: 0.23'

# def test_cenonator_2():
#     assert cenonator(
#         'koszt $cena PLN',
#         'kwota $cena PLN brutto',
#         cena=20
#     ) == 'koszt 20 PLN\nkwota 20 PLN brutto'

# print(cenonator('koszt $cena PLN', 'kwota $cena PLN brutto', 'sumarycznie $cena', 'podatek: $podatek', cena=10,podatek=0.23))

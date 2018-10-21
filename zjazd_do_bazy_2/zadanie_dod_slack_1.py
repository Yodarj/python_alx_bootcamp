# Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w dwóch linijkach naprzemiennie,
#  np.: HELLO STRANGER! ->
# H L O S R N E !
#  E L   T A G R

def wyswietlator():
    napis = input('Podaj tekst, ziomku: ')
    napis_gora = napis[0::2]
    napis_gora = ['{} '.format(x) for x in napis_gora]
    napis_dol = napis[1::2]
    napis_dol = [' {}'.format(x) for x in napis_dol]
    print(''.join(map(str, napis_gora)))
    print(''.join(map(str, napis_dol)))


wyswietlator()

# def test_wyswietlator_1():
#     assert wyswietlator('HELLO STRANGER') ==

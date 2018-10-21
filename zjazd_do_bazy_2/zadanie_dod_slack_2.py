# Napisz program, który wczyta od użytkownika tekst, a następnie podwoi w nim co drugi znak i wyświetli wynik,
#
# np.: ALA MA PSA -> ALLA  MAA PPSAA

def czengetor():
    napis = input('Podaj tekst, ziomku: ')
    napis1 = ''
    znak = 0
    for i in napis:
        if znak % 2 != 0:  # and napis.index(i) != 0:
            napis1 += i * 2
        else:
            napis1 += i
        znak += 1
    return napis1


print(czengetor())

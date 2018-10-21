# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli kwadrat z gwiazdek o długości boku X,
#
#  np.: 4 ->
#
# ****
# *    *
# *    *
# ****

def kwadrator():
    x = int(input('Podaj liczbę całkowitą: '))
    y = 0
    print(" *" * x)
    while y < x:
        print(' *',' *', sep='  '*(x-2))
        y += 1
    print(" *" * x)


kwadrator()

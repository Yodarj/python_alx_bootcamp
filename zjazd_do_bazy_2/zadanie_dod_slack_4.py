# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli romb o wysokości 2X,
#
# np.: 2 ->
#
#  /\
# /  \
# \  /
#  \/

x = int(input('Podaj liczbę całkowitą: '))

def rombator_gora(x):
    y = 0
    z = x
    while y < 2*x:
        if y < x:
            print(' '*z, '/','\\', sep=' '*(y))
        z -= 2
        y += 1

def rombator_dol(x):
    y = 0
    while y < 2*x:
        if y >= x:
            print('\\', '/', sep=' ' * (y))

        y += 1


def rombator():
    rombator_gora(x)
    # rombator_dol(x)


rombator()

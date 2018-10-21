def upper_diamond (level, length):
    if level <= length:
        print(' ' * (length - level), end='')
        print('/', end='')
        print(' ' * 2 * (level - 1), end='')
        print('\\')
        upper_diamond(level + 1, length)

def lower_diamond (level, length):
    if level <= length:
        print(' ' * (level - 1), end='')
        print('\\', end='')
        print(' ' * 2 * (length - level), end='')
        print('/')
        lower_diamond(level + 1, length)

def diamond(length):
    upper_diamond(1, length)
    lower_diamond(1, length)

length = int(input("Podaj liczbę całkowitą: "))
diamond(length)
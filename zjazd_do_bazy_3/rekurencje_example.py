def silnia(liczba):
    if liczba == 1:
        return 1
    return liczba*silnia(liczba-1)

print(silnia(666))

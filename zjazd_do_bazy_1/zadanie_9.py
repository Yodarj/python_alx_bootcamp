import datetime as dt

rok = int(input('Podaj rok urodzenia: '))
rok_teraz = dt.datetime.today().year

if rok_teraz - rok >= 18:
    print('Jesteś pełnoletni!')
else:
    print('Nie kupuj piwa')
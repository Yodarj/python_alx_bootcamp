dl = float(input('Podaj dlugosc w cm: ').replace(',','.'))
sz = float(input('Podaj szerokosc w cm: ').replace(',','.'))
gl = float(input('Podaj glebokosc w cm: ').replace(',','.'))
25,
poj = dl * sz * gl

print('Czy większa od litra?')

if poj > 1000:
    print('Tak, pojemność wynosi', round(poj/1000,2),'litrów')
else:
    print('Nie, pojemność wynosi', round(poj/1000,2),'litra')

tra = input('Czy chcesz przetłumaczyć? ')

if tra == 'tak':
    print('Wejdź na http://www.translate.google.com')
else:
    print('Alert')

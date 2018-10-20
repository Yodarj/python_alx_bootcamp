def przywitaj_sie(x, y, z, c):
    print('Cześć', x, y, z, c)

lista_osob = [
    {
        'x': "Exo",
        'y': "kuku",
        'z': "bebe",
        'c': "asd"
    }
]

for osoba in lista_osob:
    przywitaj_sie(osoba['x'], osoba['y'], osoba['z'], osoba['c'])
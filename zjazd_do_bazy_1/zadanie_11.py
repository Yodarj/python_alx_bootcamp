print('Podaj wymiary planszy:')






poz_x = int(input('Podaj pozycję X gracza: '))
poz_y = int(input('Podaj pozycję Y gracza: '))

if poz_x in range(11) and poz_y in range(11):
    pozycja = 'lewym dolnym rogu'
elif poz_x in range(11) and poz_y in range(11, 90):
    pozycja = 'lewej krawędzi'
elif poz_x in range(11) and poz_y in range(90, 101):
    pozycja = 'lewym górnym rogu'
elif poz_x in range(11, 90) and poz_y in range(11):
    pozycja = 'dolnej krawędzi'
elif poz_x in range(11, 90) and poz_y in range(11, 90):
    pozycja = 'centrum'
elif poz_x in range(11, 90) and poz_y in range(90, 101):
    pozycja = 'górnej krawędzi'
elif poz_x in range(90, 101) and poz_y in range(11):
    pozycja = 'prawym dolnym rogu'
elif poz_x in range(90, 101) and poz_y in range(11, 90):
    pozycja = 'prawej krawędzi'
elif poz_x in range(90, 101) and poz_y in range(90, 101):
    pozycja = 'prawym górnym rogu'
else:
    pozycja = 'miejscu poza planszą'

print(f'''Pozycja X gracza: {poz_x}
Pozycja Y gracza: {poz_y}
Gracz znajduję się w {pozycja}
''')
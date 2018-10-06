print('Podaj wymiary planszy:')
x = int(input('Podaj szerokość: '))
y = int(input('Podaj długość: '))

print(f'''To plansza o wymiarach {x} x {y}''')

poz_x = int(input('Podaj pozycję X gracza: '))
poz_y = int(input('Podaj pozycję Y gracza: '))

if poz_x in range(int(0.11*x)) and poz_y in range(int(0.11*y)):
    pozycja = 'lewym dolnym rogu'
elif poz_x in range(int(0.11*x)) and poz_y in range(int(0.11*y),int(0.9*y)):
    pozycja = 'lewej krawędzi'
elif poz_x in range(int(0.11*x)) and poz_y in range(int(0.9*y), int(y+1)):
    pozycja = 'lewym górnym rogu'
elif poz_x in range(int(0.11*x), int(0.9*x)) and poz_y in range(int(0.11*y)):
    pozycja = 'dolnej krawędzi'
elif poz_x in range(int(0.11*x), int(0.9*x)) and poz_y in range(int(0.11*y), int(0.9*y)):
    pozycja = 'centrum'
elif poz_x in range(int(0.11*x), int(0.9*x)) and poz_y in range(int(0.9*y), (y+1)):
    pozycja = 'górnej krawędzi'
elif poz_x in range(int(0.9*x), (x+1)) and poz_y in range(int(0.11*y)):
    pozycja = 'prawym dolnym rogu'
elif poz_x in range(int(0.9*x), (x+1)) and poz_y in range(int(0.11*y), int(0.9*y)):
    pozycja = 'prawej krawędzi'
elif poz_x in range(int(0.9*x), (x+1)) and poz_y in range(int(0.9*y), (y+1)):
    pozycja = 'prawym górnym rogu'
else:
    pozycja = 'miejscu poza planszą'

print(int(0.1*x), 'vs', poz_x)
print(int(0.1*y), 'vs', poz_y)
print(int(0.9*x), 'vs', poz_x)
print(int(0.9*y), 'vs', poz_y)



print(f'''Pozycja X gracza: {poz_x}
Pozycja Y gracza: {poz_y}
Gracz znajduje się w {pozycja}
''')
liczba = float(input("Podaj liczbę: ").replace(',','.'))

x = liczba > 10
y = liczba <= 15
z = int(liczba) % 2 == 0

print(f'''Większa od 10: {x}
Mniejsza równa 15: {y}
Podzielna przez 2: {z}
''')

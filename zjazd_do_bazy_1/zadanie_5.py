miasto_a = input("Podaj miasto, z którego wyjeżdżasz: ")
miasto_b = input("Podaj miasto, do którego jedziesz: ")
dystans = float(input("Ile to będzie km? ").replace(',','.'))
cena_paliwa = float(input("Podaj średnią cenę paliwa: ").replace(',','.'))
spalanie = float(input("Ile auto pali na 100 km? ").replace(',','.'))

wyliczenie = round(dystans/100 * spalanie * cena_paliwa,2)

print(f'''
Miasto A: {miasto_a}
Miasto B: {miasto_b}
Dystans na trasie {miasto_a} - {miasto_b}: {dystans} km
Cena paliwa: {cena_paliwa}
Spalanie na 100 km: {spalanie}

Koszt przejazdu na trasie {miasto_a}-{miasto_b} to {wyliczenie} PLN
''')

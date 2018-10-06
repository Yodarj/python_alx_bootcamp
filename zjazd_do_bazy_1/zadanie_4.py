print("Podaj cenę za kilogram:")
cenakg = float(input().replace(',','.'))

print("Podaj wagę w kilogramach:")
waga = float(input().replace(',','.'))

naleznosc = cenakg*waga

print(f'''
Cena za kg: {cenakg}
Waga w kg: {waga}
Należność: {naleznosc}
''')

#print('a', 'b', sep='\n')
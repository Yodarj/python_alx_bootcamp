dictionary = {'wódka':5.63,'amarena':2.22}

# rzecz = input('Wpisz co kupujesz: ')
# cena = float(input('Wpisz w jakiej cenie: ').replace(',','.'))
#
# dictionary[rzecz] = cena
#
# print(dictionary)
#
# rzecz = input('Wpisz co kupujesz: ')
# cena = float(input('Wpisz w jakiej cenie: ').replace(',','.'))
#
# dictionary[rzecz] = cena
#
# print(dictionary)

warzywo = input('Wpisz co kupujesz: ')
waga = float(input('Wpisz ile kupujesz w kg ').replace(',','.'))

print(f'Kupujesz {warzywo} za {dictionary[warzywo]*waga}')
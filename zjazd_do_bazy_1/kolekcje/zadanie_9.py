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



while True:
    warzywo = input('''Wpisz co kupujesz. 
Wpisz "show", aby pokazać wszystkie dostępne produkty. 
Wpisz "koniec", aby zakończyć:
''')
    if warzywo == 'show':
        print(dictionary.keys())
    elif warzywo == 'koniec':
        break
    else:
        waga = float(input('Wpisz ile kupujesz w kg ').replace(',','.'))
        print(f'Kupujesz {warzywo} za {dictionary[warzywo]*waga}')
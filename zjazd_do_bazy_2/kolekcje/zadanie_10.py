napis = input('Podaj nazwę: ')
dictionary = {}
# napis.count('t')
#
# print(napis.count('t'))

#zliczyć
for i in napis:
    dictionary[i] = napis.count(i)

#wyświetlić
for cos in dictionary:
    print(cos, dictionary[cos])
#print(i, dictionary[i])

#--------------------------------------------------

napis = input('Podaj nazwę: ')
licznik = {}

for litera in napis:
    if litera in licznik:
        licznik[litera] = licznik[litera]+ 1
    else:
        licznik[litera] = 1

for litera in licznik:
    print(f'Litera: {litera} wystąpiła {licznik[litera]} razy')

# --------------------------------------------------

napis = input('Podaj nazwę: ')
licznik = {}

for litera in napis:
    licznik[litera] = licznik.get[litera,0] + 1

for litera in licznik:
    print(f'Litera: {litera} wystąpiła {licznik[litera]} razy')

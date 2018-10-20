napis = input('Podaj nazwę: ')
dictionary = {}
# napis.count('t')
#
# print(napis.count('t'))


for i in napis:
    dictionary[i] = napis.count(i)

for cos in dictionary:
    print(cos, dictionary[cos])
#print(i, dictionary[i])

#--------------------------------------------------

napis = input('Podaj nazwę: ')
dictionary = {}
napis = input('Podaj nazwę: ')
dictionary = {}
# napis.count('t')
#
# print(napis.count('t'))


for i in napis:
    napis.count(i)
    dictionary[i] = dictionary.get(i, 0)

print(dictionary)
#print(i, dictionary[i])
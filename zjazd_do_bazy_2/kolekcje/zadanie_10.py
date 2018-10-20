napis = input('Podaj nazwę: ')

# napis.count('t')
#
# print(napis.count('t'))


for i in napis:
    dictionary = {i:napis.count(i)}
    print(i, dictionary[i])
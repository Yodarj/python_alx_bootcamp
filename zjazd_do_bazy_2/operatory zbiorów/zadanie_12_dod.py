lista = [5, 2, 1, 4, 3]

print('Przed: ', lista)

for i in range(len(lista)):
    index_minimum = i
    # print(lista[i:])
    for j in range(i+1, len(lista)):
        if lista[j] < lista [index_minimum]:
            index_minimum = j
    lista[i], lista[index_minimum] = lista[index_minimum], lista[i]
    print('i: ', i, 'lista: ', lista)
print('Po: ', lista)



# print(min(lista))
# for i in lista:
#     print(min(lista))
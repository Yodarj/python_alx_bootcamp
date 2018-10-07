lista = [5, 2, 1, 4, 3]

y = lista.index(max(lista))
z = lista.index(min(lista))
found = max(lista) in lista

lista[y], lista[z] = lista[z], lista[y]

print(lista)




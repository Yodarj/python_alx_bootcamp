lista_1 = [x / 10 for x in range(0, 11)]
print(lista_1)

lista_2 = [(x, x**2, x**3) for x in range(-10, 11)]
print(lista_2)

napis = ['joł', 'ziom', 'hehe', 'kelkeklekl']
lista_3 = {i:len(i) for i in napis}
print(lista_3)
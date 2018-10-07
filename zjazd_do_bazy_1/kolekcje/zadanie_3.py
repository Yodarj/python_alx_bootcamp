lista = []
i = 0
minus = 0
plus = 0
zero = 0

print('Wprowadzić max 10 liczb, wpisz stop aby zakończyć')
while i < 10:
    x = input()
    if x == 'stop':
        break
    x = int(x)
    lista.append(x)
    i += 1

# for x in lista:
#     x = input()
#     lista.append(x)
#     if len(lista) == 10:
#         break



for i in lista:
    if i < 0:
        minus += 1
    elif i > 0:
        plus += 1
    else:
        zero += 1

print(f'Ilość liczb ujemnych: {minus}')
print(f'Ilość liczb dodatnich: {plus}')
print(f'Ilość zer: {zero}')

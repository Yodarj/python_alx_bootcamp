# # # argsy!!
# #
# # def foo2(*args, cena=10):
# #     print(args)
# #     print(cena)
# #
#
# # foo2(5)
#
# def foo3(x, *args, **kwargs):
#     # print('args', args)
#     # print('cena', x)
#     # print('kwargs', kwargs)
#
#     for text in args:
#         print(text)
#     for key in kwargs:
#         print(key, kwargs[key])
#
# x = [1231123,1231,51231,1512]
# slownik = {'cena':10, 'podatek':0.23}
#
# foo3(10, *x, **slownik)

# ----------------------------------------------------------------------------------------------------------------------

def podzielna_przez_2(x):
    return x % 2 == 0

def podzielna_przez_3(x):
    return x % 3 == 0

print(podzielna_przez_2(12))
print(podzielna_przez_2(11))

y = lambda x: x % 2 == 0

print(y(2))
print(y(4))
print(y(5))


def wybierz(dane, warunek):
    out = []
    for element in dane:
        if warunek(element):
            out.append(element)
    return out


lista = [1, 2, 3, 4, 5, 12, 132, 1512, 241]

print(wybierz(lista, lambda x: x % 2 == 0))
print(wybierz(lista, podzielna_przez_2))
print(wybierz(lista, lambda x: x % 3 == 0))
print(wybierz(lista, podzielna_przez_3))

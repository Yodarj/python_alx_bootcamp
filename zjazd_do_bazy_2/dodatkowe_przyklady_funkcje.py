# # argsy!!
#
# def foo2(*args, cena=10):
#     print(args)
#     print(cena)
#

# foo2(5)

def foo3(x, *args, **kwargs):
    # print('args', args)
    # print('cena', x)
    # print('kwargs', kwargs)

    for text in args:
        print(text)
    for key in kwargs:
        print(key, kwargs[key])

x = [1231123,1231,51231,1512]
slownik = {'cena':10, 'podatek':0.23}

foo3(10, *x, **slownik)
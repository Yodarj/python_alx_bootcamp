def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Różny kształt")

    wynik = []
    lista = []
    for row_i in range(len(a)):
        for row_c in range(len(a[0])):
            lista.append(a[row_i][row_c] + b[row_i][row_c])
        wynik.append(lista)
        lista = []

    return wynik


def sub_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Różny kształt")

    wynik = []
    lista = []
    for row_i in range(len(a)):
        for row_c in range(len(a[0])):
            lista.append(a[row_i][row_c] - b[row_i][row_c])
        wynik.append(lista)
        lista = []

    return wynik

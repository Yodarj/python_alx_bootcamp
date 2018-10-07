i = -1
suma = 0
znalezione_max = None
znalezione_min = None
imin = None
imax = None


while True:

    i += 1
    dane_wej = input('Podaj liczbę lub wpisz stop, aby zakończyć: ')
    if dane_wej.lower() == 'stop':
        break
    elif dane_wej == '':
        raise ValueError('Nie wprowadziłżeś żadnej liczby')
    else:
        liczba = float(dane_wej)
        if i == 0:
            znalezione_max = liczba
            znalezione_min = liczba
            imax = i
            imin = i
        else:
            if liczba > znalezione_max:
                znalezione_max = liczba
                imax = i
            elif liczba < znalezione_min:
                znalezione_min = liczba
                imin = i
        suma = suma + liczba

if i == 0:
    print("Brak liczb do wyliczeń")
    exit()
else:
    srednia = suma/i

print(f'Ilość wpisanych liczb to {i}')
print(f'Najmniejsza liczba to: {znalezione_min} i była to {imin+1} liczba')
print(f'Największa liczba to: {znalezione_max} i była to {imax+1} liczba')
print(f'Suma wszystkich liczb wynosi: {suma}, zaś średnia biorąc pod uwagę {i} liczb wynosi {srednia}')


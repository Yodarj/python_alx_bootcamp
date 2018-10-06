liczba_1 = float(input('Podaj pierwszą liczbę: ').replace(',','.'))
liczba_2 = float(input('Podaj drugą liczbę: ').replace(',','.'))
operacja = input('Podaj rodzaj operacji: ')

if operacja == '+':
    print('Wynik: ', liczba_1 + liczba_2)
elif operacja == '-':
    print('Wynik: ', liczba_1 - liczba_2)
elif operacja == '/' and liczba_2 == 0:
    print('cholero nie dziel przez zero')
elif operacja == '/':
    print('Wynik: ', liczba_1 / liczba_2)
elif operacja == '*':
    print('Wynik: ', liczba_1 * liczba_2)
else:
    print('błendnydasdasd znak operacji')

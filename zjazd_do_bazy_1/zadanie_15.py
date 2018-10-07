from random import randint

# rozmiary planszy
pl_x = 10
pl_y = 10

# położenie skarbu
skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

# położenie gracza
gracz_x = randint(1, 10)
gracz_y = randint(1, 10)

# położenie smoka
smok_x = randint(1, 10)
smok_y = randint(1, 10)

# odległość od skarbu
od_skarbu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

print(f'Graczu, jesteś w punkcie {gracz_x} x {gracz_y}')

print(f'Poruszasz się przy pomocy klawiszy w a s d')

print(f'Musisz znaleźć skarb. Ale uważaj!!! Jeśli zrobisz więcej niż 10 kroków pojawi się smok. Wtedy będzie buba! ON CIĘ ZJEEE')

#print(f'skarb {skarb_x} x {skarb_y}')

liczba_ruchow = 0

while True:
    # obliczanie i zbieranie ruchu
    min_ruch_przed = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    ruch = input(f'W którą stronę chcesz iść? ')

    #wskaźniki
    if ruch.lower() == 'w':
        gracz_y += 1
        print(f'Teraz jesteś w punkcie {gracz_x} x {gracz_y}')
    elif ruch.lower() == 'a':
        gracz_x -= 1
        print(f'Teraz jesteś w punkcie {gracz_x} x {gracz_y}')
    elif ruch.lower() == 's':
        gracz_y -= 1
        print(f'Teraz jesteś w punkcie {gracz_x} x {gracz_y}')
    elif ruch.lower() == 'd':
        gracz_x += 1
        print(f'Teraz jesteś w punkcie {gracz_x} x {gracz_y}')
    else:
        print('głupi')

    # obliczenie ilości ruchu i min liczby ruchów po
    min_ruch_po = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    liczba_ruchow += 1

    # sprawdzenie pozycji gracza względem planszy - czy poza?
    if gracz_x > 10 or gracz_x < 1 or gracz_y > 10 or gracz_y < 1:
        print('Jesteś poza planszą, odpadasz <szatański śmiech>')
        break

    # sprawdzenie skarbu
    if min_ruch_po == 0:
        print('masz skarb')
        break

    # sprawdzenie pozycji względem poprzedniej
    if min_ruch_po > min_ruch_przed:
        print('dalej')
    elif min_ruch_po < min_ruch_przed:
        print('bliżej')
    else:
        print('zunk')

    # sprawdzenie liczby ruchów, czy zmienić skarb?
    if liczba_ruchow > 2 * od_skarbu:
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        print("Skarb ma nowe położenie, osiołku")
        od_skarbu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    # # teraz dochodzi smok
    # if liczba_ruchow > 10 and liczba_ruchow <=30:
    #     print("Panie kolego, smok nadchodzi")
    #     print(f'Znajduje się w miejscu {smok_x} x {smok_y}')
    #     print(f'Ale zapierdala jak dziki!!')
    # elif liczba_ruchow > 30:
    #     print('Smok zaczyna zjadać planszę!!')
    # elif liczba_ruchow > 31:
    #     print('plansza zjedzona, łosiu')
    #     exit()

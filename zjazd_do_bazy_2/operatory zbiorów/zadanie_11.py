zbior_liczb = {}

while True:
    liczba = input("Podaj liczbę. Aby zakończyć, wpisz done: ")
    if liczba == 'done':
        break
    else:
        int(liczba)
        zbior_liczb[liczba] = zbior_liczb.get(liczba,0) + 1

for lic in zbior_liczb:
    print(f' Liczba {lic} występuje {zbior_liczb[lic]} razy')
# Napisz program "odsetki.py",
# który obliczy stan konta za N lat,
# gdzie stan początkowy konta wynosi SPK,
# a stopa oprocentowania P % rocznie
# (obowiązuje roczna kapitalizacja odsetek).
# N, SPK i P podaje użytkownik programu.

def odsetki(n, spk, p):
    skk = spk * (1+p/100)**n
    return skk


n = int(input("Podaj liczbę lat: "))
spk = int(input("Podaj stan konta: "))
p = float(input("Podaj oprocentowanie: ").replace(',','.'))

print(f'''Ziomku, na początku byłeś biedakiem i miałeś {spk} PLN. 
Dałeś mi hajs, inwestowałem przez {n} lat z oprocentowaniem {p}% i dzięki mnie jesteś bogaty.
Masz teraz {round(odsetki(n, spk, p),2)}. 
Zarobiłeś {round(odsetki(n, spk, p),2)-spk}
Pan jest z Tobą''')
#print(round(odsetki(n, spk, p),2))
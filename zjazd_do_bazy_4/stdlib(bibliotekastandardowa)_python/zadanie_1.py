import json

pracownicy = []
zbior = {}

czynnosc = input('Co chcesz zrobić? [d - dodaj, w - wypisz]')

if czynnosc == 'd':
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = input("Rok urodzenia: ")
    pensja = input("Pensja: ")
    with open("pracownicy.json") as f:
        pracownicy.append(nowy_pracownik)
        json.dump(pracownicy, f)

elif czynnosc == 'w':
    with open("pracownicy.json") as f:
        print(json.dump(f))

else:
    'Tym tym tym - nie ma takiej czynności'



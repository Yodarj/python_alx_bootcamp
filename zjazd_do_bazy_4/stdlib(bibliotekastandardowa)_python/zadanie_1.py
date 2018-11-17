import json

czynnosc = input('Co chcesz zrobić? [d - dodaj, w - wypisz]')

if czynnosc == 'd':
    with open("pracownicy.json") as f:
        pracownicy = json.load(f)
        pracownicy.append(
            [input("Imię: "),
             input("Nazwisko: "),
             input("Rok urodzenia: "),
             input("Pensja: "),
        ]
        )

elif czynnosc == 'w':
    with open("pracownicy.json") as f:
        json.dump(f)

else:
    'Tym tym tym - nie ma takiej czynności'



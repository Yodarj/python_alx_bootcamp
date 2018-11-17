import json
try:
    with open('pracownicy.json') as f:
        pracownicy = json.load(f)
except:
    pracownicy = []

action = input('Co chcesz zrobić? [d - dodaj, w - wypisz]')

if action == 'd':
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownik ={
        "imie": imie,
        "nazwisko": nazwisko,
        "rok urodzenia": rok_urodzenia,
        "pensja": pensja,
        }
    pracownicy.append(pracownik)
    with open("pracownicy.json", "w") as f:
        json.dump(pracownicy, f)



elif action == 'w':
    print("Pracownicy")

    for i, pracownik in enumerate(pracownicy, start=1):
        print(f'''-[{i}] {pracownik['imie']} {pracownik['nazwisko']} - rok: {pracownik['rok urodzenia']}, pensja: {pracownik['pensja']} PLN''')

else:
    'Tym tym tym - nie ma takiej czynności'
produkty = {'ziemniaki':2, 'bataty':4,'pomidory':6}
magazyn = {'ziemniaki':10, 'bataty':10,'pomidory':10}
do_zaplaty = 0
paragon = {}

while True:
    print("-"*40)
    print('Nasz zielarz oferuje:')
    for produkt in produkty:
        cena = produkty[produkt]
        print(f' - {produkt} - {cena} PLN w ilości {magazyn[produkt]} kg')

    komenda = input('Co chcesz uczynić: [k]upić, [d]odać, [koniec] by przerwać zakupy ')
    if komenda == 'koniec':
        break
    elif komenda == 'k':
        produkt_wybrany = input('Co chcesz kupić?')
        if produkt_wybrany not in produkty:
            print('Ty ty ty, nie ma taakiego numeru')
            continue
        else:
            waga = float(input(f'Ile chcesz kupić wybranego produktu [{produkt_wybrany}]:').replace(',','.'))
            if magazyn[produkt_wybrany] < waga:
                print(f'Za mało produktu, na stanie pozostało tylko {magazyn[produkt_wybrany]} kg produktu [{produkt_wybrany}]')
            else:
                koszt = produkty[produkt_wybrany] * waga
                do_zaplaty += koszt
                magazyn[produkt_wybrany] -= waga
                if produkt_wybrany in paragon:
                    paragon[produkt_wybrany] += koszt
                else:
                    paragon[produkt_wybrany] = koszt
    elif komenda == 'd':
        produkt_do_magazyn = input('Jaki produkt chcesz dodać? ')
        if produkt_do_magazyn not in magazyn:
            magazyn[produkt_do_magazyn] = 0
            cena_nowego_produktu = float(input('Za ile to sprzedajemy? '))
            produkty[produkt_do_magazyn] = cena_nowego_produktu
        dod_waga = float(input('Ile chcesz dodać produktu? ').replace(',','.'))
        magazyn[produkt_do_magazyn] += dod_waga
    else:
        print("Cooooo????!!!")


for produkt in paragon:
    print(f'- {produkt} - {koszt}')

print(f'Będzie Cię to kosztowaać {do_zaplaty} peelenów')


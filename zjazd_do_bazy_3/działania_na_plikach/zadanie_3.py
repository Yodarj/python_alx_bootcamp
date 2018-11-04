import sys

try:
    nazwa = sys.argv[1]
except:
    # print("Podaj plik, ziomek")
    # quit()
    nazwa = 'emails.txt'

full_list = []

with open(f"dane/{nazwa}", encoding='utf-8') as f:
    for email in f:
        email = email.lower().strip()
        if email.count('@') == 1 and email not in full_list:
            full_list.append(email)
        else:
            continue

try:
    nowa_nazwa = sys.argv[2]
except:
    print("Nie podałeś nazwy drugiego pliku. Plik będzie się zwał 'nowe_maile.txt'")
    nowa_nazwa = 'nowe_maile.txt'



with open(f'dane/{nowa_nazwa}', 'w') as f:
    for i in sorted(full_list):
        f.write(i)
        f.write('\n')




import csv

with open("dane/train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    dlugosci = {}
    for row in data:
        dlugosci[row['Survived']] = dlugosci.get(row['Survived'],0 ) +1

    przezylo = dlugosci['1']
    zginelo = dlugosci['0']

    print(f'''Przeżyło z ogółu: {100*przezylo/(przezylo+zginelo)}''')
    print(f'''Zginęło z ogółu: {100*zginelo/(przezylo+zginelo)}''')


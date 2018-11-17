import json
import urllib.request

kod = input("Jaką walutę chcesz kupić (podaj skrót): ")
ilosc = int(input("Ile chcesz kupić? "))

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A?format=json") as f:
    kursy = json.loads(f.read())

ceny = kursy[0]['rates']

for c in ceny:
    if c['code'] == kod:
        wynik = round(ilosc*c['mid'],2)

print(wynik)








# rates = kursy[0]['rates']
#
# for r in rates:
#     print(f'''{r['code']} - {r['mid']}''')



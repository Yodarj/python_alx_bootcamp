import json
import urllib.request
import datetime as dt

miasto = input("Podaj miasto [angielska nazwa]: ")

temat_data = input("Wpisz [dzisiaj] lub [inna data]: ")
if temat_data == 'dzisiaj':
    data = f'''{dt.datetime.today().year}/{dt.datetime.today().month}/{dt.datetime.today().day}'''

else:
    rok = int(input("Podaj rok (między 2013 a obecnym): "))
    miesiac = int(input("Podaj miesiąc: "))
    dzien = int(input("Podaj dzień: "))
    if miesiac < 10:
        miesiac = '0'+str(miesiac)
    else:
        str(miesiac)

    if dzien < 10:
        dzien = '0'+str(dzien)
    else:
        str(dzien)
    data = f'''{rok}/{miesiac}/{dzien}'''


with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/search/?query={miasto}''') as f:
    dane_miasta = json.loads(f.read())
    id_miasta = dane_miasta[0]['woeid']


with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/{id_miasta}/{data}''') as p:
    pogoda = json.loads(p.read())

dane_z_podanej_daty = pogoda[0]

for key in dane_z_podanej_daty:
    if key in ('applicable_date', 'the_temp', 'air_pressure', 'humidity'):
        print(key, '-', dane_z_podanej_daty[key])
    else:
        continue

odpowiedz = input("Czy odpowiedź jest satysfakcjonująca?")

if odpowiedz == 'tak':
    input("Press click to quit")
else:
    input("Cokolwiek zrobisz, będzie źle")



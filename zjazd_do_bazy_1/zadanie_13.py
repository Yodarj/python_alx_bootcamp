dni_tygodnia = int(input("Podaj liczbę dni w tym tygodniu: "))
day = 1
suma = 0

while day <= dni_tygodnia:
    temp = int(input(f'''Podaj temperaturę {day} dnia: '''))
    suma = suma + temp
    day += 1


sr = round(suma/dni_tygodnia,2)
print(f'''Średnia temperatura w tym tygodniu wyniosła {sr}''')

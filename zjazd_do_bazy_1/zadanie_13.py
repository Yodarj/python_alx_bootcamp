dni_tygodnia = int(input("Podaj liczbę dni w tym tygodniu: "))
day = 1
suma = 0

while day <= dni_tygodnia:
    temp = int(input(f'''Podaj temperaturę {day} dnia: '''))
    suma = suma + temp
    if day == 1:
        dzien_tygodnia = 'pon'
        temp_pon = temp
    elif day == 2:
        dzien_tygodnia = 'wto'
        temp_wto = temp
    elif day == 3:
        dzien_tygodnia = 'sro'
        temp_sro = temp
    elif day == 4:
        dzien_tygodnia = 'czw'
        temp_czw = temp
    elif day == 5:
        dzien_tygodnia = 'pia'
        temp_pia = temp
    elif day == 6:
        dzien_tygodnia = 'sob'
        temp_sob = temp
    elif day == 7:
        dzien_tygodnia = 'ndz'
        temp_ndz = temp
    else:
        dzien_tygodnia = 'nie ma takiego numeru'
        temp_no = temp
    day += 1


sr = round(suma/dni_tygodnia,2)
print(f'''Średnia temperatura w tym tygodniu wyniosła {sr}''')
print(f'Temperatura maksymalna wyniosła {max([temp_pon, temp_wto, temp_sro, temp_czw, temp_pia, temp_sob, temp_ndz])}')
print(f'Temperatura minimalna wyniosła {min([temp_pon, temp_wto, temp_sro, temp_czw, temp_pia, temp_sob, temp_ndz])}')
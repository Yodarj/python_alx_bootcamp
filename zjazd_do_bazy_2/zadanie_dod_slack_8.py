# Napisz program "numer.py", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:
# a) znaki nie będące cyframi mają być ignorowane
# b) konwertujemy cyfry, nie liczby, a zatem:
# - 911 to "dziewięć jeden jeden"
# - 1100 to "jeden jeden zero zero"

def numerologia(ciag):
    ciag = str(ciag)
    tekst = ''
    przypisanie = {
        1:'jeden',
        2:'dwa',
        3:'trzy',
        4:'cztery',
        5:'pięć',
        6:'sześć',
        7:'siedem',
        8:'osiem',
        9:'dziewięć',
        0:'zero',
    }
    ciag = [int(x) for x in ciag]
    for liczba in ciag:
        tekst += przypisanie[liczba]
        tekst += ' '
    print(tekst)

ciag = int(input("Podaj ciung: "))
numerologia(ciag)
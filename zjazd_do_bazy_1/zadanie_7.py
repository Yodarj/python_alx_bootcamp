import ctypes as ct

#liczba = int(input('Podaj liczbę: '))

#print("Sprawdzenie: ", liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10 or liczba == 7)

liczba = 14

def mbox(title, text, style):
    return ct.windll.user32.MessageBoxW(0, text, title, style)

if liczba > 10 and liczba % 2 == 0:
    mbox('Your title', '''lama lama lama lama lama lama 
    lama 
    lama 
    lama 
    lama 
    lama 
    lama 
    lama 
    lama 
    ''', 1)
else:
    mbox('Your title', 'pupa', 1)

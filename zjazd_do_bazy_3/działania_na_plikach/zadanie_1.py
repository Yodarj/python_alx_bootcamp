import sys

try:
    sys.argv[1]
except:
    print("Podaj plik, ziomek")
    quit()

nazwa = sys.argv[1]
try:
    with open(f'dane/{nazwa}', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')

except FileNotFoundError:
    print('Nie ma ziomeczku takiego pliczeczku')

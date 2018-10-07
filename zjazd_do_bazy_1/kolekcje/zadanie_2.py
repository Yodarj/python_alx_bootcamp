# zebranie liczb (nie więcej niż 10)

print('Proszę podać 10 liczb')
i = 0
x = []

while i < 10:
    x.append(int(input()))
    i += 1

# x = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]

# obliczenie średniej
print('dlugosc listy', len(x))
y = sum(x)
sr = y / len(x)
print('srednia', sr)

# wypisanie wyniku

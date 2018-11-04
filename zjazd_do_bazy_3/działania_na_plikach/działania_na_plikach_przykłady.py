# file = open("dane/file.csv")
# print(file.read())
# file.close()


with open("dane/file.csv") as f:
    print(f.read())

with open("dane/nowy_plik.txt", 'w', encoding='utf-8') as f:
    f.write('jakiś tekst')
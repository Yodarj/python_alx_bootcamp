# zbior_liczb = {}
# liczby_parzyste_mr_100 = {}
# liczby_parzyste_w_100 = {}
#
# while True:
#     liczba = input("Podaj liczbę. Aby zakończyć, wpisz done: ")
#     if liczba == 'done':
#         break
#     else:
#         liczba = int(liczba)
#         zbior_liczb[liczba] = zbior_liczb.get(liczba, 0) + 1
#
# for lic in zbior_liczb:
#     print(f' Liczba {lic} występuje {zbior_liczb[lic]} razy')
#
# a = set(zbior_liczb.keys())
#
# parz_mr_100 = 0
# parz_w_100 = 0
#
# for i in a:
#     if i % 2 == 0 and i <= 100:
#         parz_mr_100 += 1
#         liczby_parzyste_mr_100[i] = liczby_parzyste_mr_100.get(i, 0) + 1
#     elif i % 2 == 0 and i > 100:
#         parz_w_100 += 1
#         liczby_parzyste_w_100[i] = liczby_parzyste_w_100.get(i, 0) + 1
#     else:
#         continue
#
# print("-"*40)
# print(f'Ilość parzystych mniejszych lub równych 100 wynosi {parz_mr_100}')
#
# print(set(liczby_parzyste_mr_100.keys())
#
# print(f'Ilość liczb parzystych większych od 100 wynosi {parz_w_100}')
#
# print(set(liczby_parzyste_w_100.keys()))
#
# print(liczby_parzyste_mr_100)
# print(liczby_parzyste_w_100)

print("-"*40)
liczby = set()

while True:
    komenda = input("Wprowadź liczbę lub k, aby zakończyć: ")
    if komenda == 'k':
        break
    liczba = int(komenda)
    liczby.add(liczba)

print(liczby & set(range(2,101,2)))
nazwa = input('Daj jakąś nazwę: ')

liczba_samog = 0

for lit in nazwa.lower():
    if lit in ('a', 'e', 'i', 'o', 'u', 'y'):
        liczba_samog += 1

print(f'Liczba samogłosek w podanym słowie: {liczba_samog}')

napis = input('Wpisz słowo i oznacz <> co chcesz wyliczyć: ')

x = napis.find('<')
y = napis.find('>')

# print(x)
# print(y)

napisn = napis[x+1:y]
print(f'Długość wyrazu pomiędzy < i > to: {len(napisn)}')


przez_trzy = 0
przez_piec = 0


for i in range(101):
    if i%3 == 0:
        przez_trzy += 1
    elif i%5 == 0:
        przez_piec += 1

print(przez_trzy)
print(przez_piec)
print(przez_piec+przez_trzy)


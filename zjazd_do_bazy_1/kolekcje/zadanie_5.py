# for el in range(10):
#     print(el, el*el)
for i in range (10):
    print("  ", f'{i:2}', end="")

print()
print()

for y in range(10):
    print(y, end='\t')
    for x in range(10):
        print(x*y, end='\t')
    print()

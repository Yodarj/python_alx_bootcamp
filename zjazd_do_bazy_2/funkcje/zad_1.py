def czy_jest_pierwsza(x):
    for i in range(1,x):
        if x % i == 0 and x == i:
            print(False)
            break
        else:
            print(True)
            break


czy_jest_pierwsza(10)

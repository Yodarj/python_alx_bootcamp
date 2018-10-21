def romb(x):
    i = 1
    while i <= 2*x:
        j = 1
        napis = ''
        while j <= 2*x:
            if i==x-j+1 or j==3*x-i+1:
                napis += '/'
            elif i==x+j or j==x+i:
                napis += '\\'
            else:
                napis += ' '
            j += 1
        i += 1
        print(napis)
    return ''


x = int(input("podaj X, ziomku: "))
print(romb(x))


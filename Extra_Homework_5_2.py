n = int(input('N = '))
i = 0
if n % 2 == 0:
    print("Input odd number")
else:
    for j in range(n, 0, -2):
        print(i * ' ' + j * '*')
        i += 1
    i -= 2
    for j in range(3, n + 1, 2):
        print(i * ' ' + j * '*')
        i -= 1
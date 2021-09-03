t = int(input())

for u in range(t):
    number = input()
    tong, tich, n, isHave = 0, 1, len(number), False
    for i in range(0, n, 2):
        tong += int(number[i])
    for i in range(1, n, 2):
        if number[i] != '0':
            isHave = True
            tich *= int(number[i])
    if not isHave:
        tich = 0
    print(tong, tich)

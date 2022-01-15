for _ in range(int(input())):
    res = -1
    number = input()
    for i in range(1000):
        if int(number) % 7 == 0:
            res = number
            break
        number = str(int(number) + int(number[::-1]))
    print(res)

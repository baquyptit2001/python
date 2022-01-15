for _ in range(int(input())):
    number = input()
    dup = number[:2]
    times = len(number) // 2
    if (number == dup * times) or (number == (dup * times) + dup[0]):
        print('YES')
    else:
        print('NO')

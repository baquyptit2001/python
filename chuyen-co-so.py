def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        tmp = int(n % b)
        if tmp > 10:
            tmp = chr(tmp - 10 + ord('A'))
        digits.append(str(tmp))
        n //= b
    return digits[::-1]


for _ in range(int(input())):
    n, b = map(int, input().split())
    res = numberToBase(n, b)
    print(''.join(res))

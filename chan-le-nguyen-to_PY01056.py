import math


def nguyenTo(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def checker(n):
    sumDigit = 0
    for i in range(0, len(number), 2):
        if int(n[i]) % 2 != 0:
            return "NO"
        sumDigit += int(n[i])
    for i in range(1, len(number), 2):
        if int(n[i]) % 2 != 1:
            return "NO"
        sumDigit += int(n[i])
    if not nguyenTo(sumDigit):
        return "NO"
    return "YES"


t = int(input())

for u in range(t):
    number = input()
    print(checker(number))

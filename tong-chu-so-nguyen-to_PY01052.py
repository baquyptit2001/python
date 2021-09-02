import math


def nguyenTo(n):
    if n < 2:
        return "NO"
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return "NO"
    return "YES"


t = int(input())

for u in range(t):
    number = input()
    sumDigit = 0
    for i in number:
        sumDigit += int(i)
    print(nguyenTo(sumDigit))

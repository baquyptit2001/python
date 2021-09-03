import math


def nguyenTo(n):
    if (n < 2):
        return "NO"
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return "NO"
    return "YES"


t = int(input())

for u in range(t):
    number = input()
    tmp = ''
    if len(number) <= 4:
        tmp = number
    else:
        tmp = number[len(number) - 1 - 3] + number[len(number) - 1 - 2] + number[len(number) - 1 - 1] + number[
            len(number) - 1]
    print(nguyenTo(int(tmp)))

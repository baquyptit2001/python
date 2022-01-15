import math


def prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1, 1):
        if n % i == 0:
            return False
    return True


def primeList(n):
    res = []
    for i in n:
        if prime(i):
            res.append(i)
    return res


inp = list(map(int, input().split()))

print(primeList(inp))

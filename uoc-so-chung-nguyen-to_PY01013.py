from math import isqrt


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1, 1):
        if x % i == 0:
            return False
    return True


def checker(x):
    if is_prime(sum([int(d) for d in str(x)])):
        return "YES"
    return "NO"


t = int(input())
for u in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    print(checker(gcd(a, b)))

import math


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1, 1):
        if n % i == 0:
            return False
    return True


t = int(input())

for i in range(t):
    n = int(input())
    count = 0
    for i in range(1, n):
        k = gcd(i, n)
        if k == 1:
            count += 1
    if prime(count):
        print("YES")
    else:
        print("NO")

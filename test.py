import math


def gcd(a, b):
    if a == 0 :
        return b
    return gcd(b%a, a)


def nguyenTo(n):
    if n<2:
        return False
    for i in range (2, math.isqrt(n)+1):
        if n%i==0:
            return False
    return True


t = int(input())
for u in range(t):
    n = int(input())
    dem = 0
    for i in range(1, n):
        if gcd(i, n):
            dem+=1
    if nguyenTo(dem):
        print("YES")
    else:
        print("NO")

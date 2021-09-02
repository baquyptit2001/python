import math

mark = [False] * 600


def nguyenTo(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def init():
    for i in range(2, 600):
        if nguyenTo(i):
            mark[i] = True


def checker(n):
    for i in range(len(n)):
        if mark[i]:
            if not mark[int(n[i])]:
                return "NO"
        else:
            if mark[int(n[i])]:
                return "NO"
    return "YES"


init()
t = int(input())

for u in range(t):
    number = input()
    print(checker(number))

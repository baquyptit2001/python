import math

prime = []


def nt(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return x > 1


def init():
    for i in range(10 ** 5):
        if nt(i):
            prime.append(i)


def check(l, r, x):
    res = r
    while l <= r:
        mid = (l + r) // 2
        if prime[mid] == x: return mid
        if prime[mid] < x:
            l = mid + 1
        else:
            res = mid
            r = mid - 1
    return res


init()
n = int(input())
a = list(int(i) for i in input().split())
a = set(a)
inc = [0]
dec = [0]
tmp = []

for i in a:
    if nt(i):
        continue
    else:
        it1 = check(0, len(prime) - 1, i)
        it2 = it1 - 1
        if it2 < 0:
            inc.append(prime[it1] - i)
        else:
            if abs(prime[it1] - i) < abs(prime[it2] - i):
                inc.append(prime[it1] - i)
            elif abs(prime[it1] - i) > abs(prime[it2] - i):
                dec.append(prime[it2] - i)
            else:
                tmp.append(i)
compare = max(max(inc), max(dec))
for i in tmp:
    it1 = check(0, len(prime) - 1, i)
    if prime[it1] - i > compare:
        inc.append(prime[it1] - i)
inc = set(inc)
dec = set(dec)
num1 = max(dec)
num2 = max(inc)
print(num1 + num2)

from math import isqrt


def isprime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1, 1):
        if n % i == 0:
            return False
    return True


n, m = input().split()
n, m = int(n), int(m)
store = []

for i in range(n):
    a = list(map(int, input().split()))
    store.append(a)
for i in store:
    for j in i:
        if isprime(j):
            print("1", end=' ')
        else:
            print("0", end=" ")
    print()

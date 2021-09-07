t = int(input())

for u in range(t):
    n, p = map(int, input().split())
    res = 0
    for i in range(p, n, p):
        while i % p == 0:
            res += 1
            i //= p
    print(res)

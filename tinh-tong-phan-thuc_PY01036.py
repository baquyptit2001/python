t = int(input())

for u in range(t):
    res = 0
    n = int(input())
    if n % 2 == 0:
        start = 2
    else:
        start = 1
    for i in range(start, n+1, 2):
        res += 1 / i
    print("{:.6f}".format(res))

t = int(input())

for u in range(t):
    n = int(input())
    tmp = 1
    count = 1
    res = 0
    while tmp < n:
        count += 1
        if (n - tmp) % count == 0:
            res += 1
        tmp += count
    print(res)

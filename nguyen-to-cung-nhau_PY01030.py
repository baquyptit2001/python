import math

n, k = [int(x) for x in input().split()]
start, end, count = 10 ** (k-1), 10 ** k, 0
for i in range(start, end):
    if math.gcd(n, i) == 1:
        print(i, end=" ")
        count += 1
        if count % 10 == 0:
            print()

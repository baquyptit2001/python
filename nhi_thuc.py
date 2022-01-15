import math

for _ in range(int(input())):
    inp = input().split()

    n = int(inp[0])
    p = float(inp[1])
    x = int(inp[2])

    res = math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

    print("{:.6f}".format(round(res, 6)))

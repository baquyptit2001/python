import math


def nguyenTo(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


n, m = [int(x) for x in input().split()]

store = []

for i in range(n):
    tmp = list(map(int, input().split()))
    store.append(tmp)
res = -1
for i in store:
    for j in i:
        if j > res and nguyenTo(j):
            res = j
if res == -1:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if store[i][j] == res:
                print("Vi tri [{}][{}]".format(i, j))

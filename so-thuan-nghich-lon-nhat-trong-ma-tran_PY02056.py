def thuanNghich(n):
    if n < 10:
        return False
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
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
        if j > res and thuanNghich(j):
            res = j
if res == -1:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if store[i][j] == res:
                print("Vi tri [{}][{}]".format(i, j))

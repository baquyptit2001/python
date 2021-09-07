n, m = [int(x) for x in input().split()]

store = []

for i in range(n):
    tmp = list(map(int, input().split()))
    store.append(tmp)
res = -1
lon_nhat, nho_nhat = store[0][0], store[0][0]
for i in store:
    for j in i:
        if j > lon_nhat:
            lon_nhat = j
        elif j < nho_nhat:
            nho_nhat = j
compare = lon_nhat - nho_nhat
for i in range(n):
    for j in range(m):
        if store[i][j] == compare:
            if res == -1:
                print(compare)
            print("Vi tri [{}][{}]".format(i, j))
            res = 1
if res == -1:
    print("NOT FOUND")

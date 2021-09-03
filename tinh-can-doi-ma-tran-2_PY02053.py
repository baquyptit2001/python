n = int(input())
store = []
for u in range(n):
    tmp = list(map(int, input().split()))
    store.append(tmp)
k = int(input())
up, down = 0, 0
for i in range(n):
    for j in range(n - 1 - i):
        up += store[i][j]
for i in range(n):
    for j in range(n - i, n):
        down += store[i][j]
res = abs(up - down)
if res <= k:
    print("YES")
else:
    print("NO")
print(res)

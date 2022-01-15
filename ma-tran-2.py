n = int(input())
store = []
for u in range(n):
    store.append([int(i) for i in input().split()])
diff = int(input())
upper, lower = 0, 0
for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            upper += store[i][j]
        if j < n - i - 1:
            lower += store[i][j]
if abs(upper - lower) <= diff:
    print("YES")
else:
    print("NO")
print(abs(upper - lower))

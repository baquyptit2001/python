n = int(input())

store = list(map(float, input().split()))
store = sorted(store)
res, count = 0, 0
for i in range(1, n):
    if store[i] != store[0] and store[i] != store[n-1]:
        res += store[i]
        count += 1
print("{:.2f}".format(res / count))

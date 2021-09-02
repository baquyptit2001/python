n = int(input())
store = list(map(int, input().split()))
res = 0
for i in range(1, n):
    if store[i] != store[i - 1]:
        res += 1
print(res)

n = int(input())
store = []
for i in range(n):
    store.append(list(map(int, input().split())))

if n == 2:
    print(n // 2, n // 2)
else:
    sum1 = 0
    for i in range(n):
        if i == n - 1:
            sum1 = sum1 + store[i][0]
        else:
            sum1 = sum1 + store[i][i + 1]
    sum2 = 0
    for i in range(1, n):
        if i == n - 1:
            sum2 = sum2 + store[i][1]
        else:
            sum2 = sum2 + store[i][i + 1]
    res = [(sum1 - sum2) // 2]
    for i in range(1, n):
        res.append(store[i - 1][i] - res[len(res) - 1])
    for i in res:
        print(i, end=' ')

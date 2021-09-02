t = int(input())

for u in range(t):
    n = int(input())
    store = list(map(int, input().split()))
    rangeArr = n // 2 + 1
    store = sorted(store)
    res = "NO"
    for i in range((n+1)//2):
        if store[i] == store[i + rangeArr - 1]:
            res = store[i]
            break
    print(res)

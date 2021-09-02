t = int(input())

for u in range(t):
    n = int(input())
    store1 = list(map(int, input().split()))
    store2 = list(map(int, input().split()))
    store1 = sorted(store1)
    store2 = sorted(store2)
    res = "YES"
    for i in range(n):
        if store1[i] > store2[i]:
            res = "NO"
            break
    print(res)

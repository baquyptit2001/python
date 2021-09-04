import collections

t = int(input())

for u in range(t):
    n = int(input())
    store = list(map(int, input().split()))
    c = collections.Counter(store)
    for i in c:
        if c[i] % 2 == 1:
            print(i)
            break

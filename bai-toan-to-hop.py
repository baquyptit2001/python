from itertools import combinations

n, k = map(int, input().split())

store = set([int(x) for x in input().split()])

store = sorted(store)

store = list(combinations(store, k))

for i in store:
    print(" ".join(map(str, i)))


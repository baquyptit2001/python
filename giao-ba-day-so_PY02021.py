t = int(input())

for u in range(t):
    m, n, p = [int(x) for x in input().split()]
    store1 = list(map(int, input().split()))
    store2 = list(map(int, input().split()))
    store3 = list(map(int, input().split()))
    isHave = False
    i, j, k = 0, 0, 0
    while i < m and j < n and k < p:
        if store1[i] == store2[j] and store3[k] == store2[j]:
            print(store1[i], end=' ')
            isHave = True
            i += 1
            j += 1
            k += 1
        elif store1[i] < store2[j]:
            i += 1
        elif store2[j] < store3[k]:
            j += 1
        else:
            k += 1
    if not isHave:
        print("NO", end='')
    print()

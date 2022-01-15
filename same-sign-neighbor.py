count, active = 0, [0, 0]

n = int(input())


store = [int(x) for x in input().split()]

for i in range(1, n):
    if store[i] * store[i - 1] > 0:
        count += 1
        active[1] = store[i]
        active[0] = store[i - 1]

if count == 0:
    print(0)
else:
    print(count, active[0], active[1])

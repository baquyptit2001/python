t = int(input())

for u in range(t):
    n = int(input())
    store = []
    roll, res, maxx = [0] * 2000, 2101, 0
    for i in range(n):
        store.append(int(input()))
    for number in store:
        roll[number] += 1
        if roll[number] > maxx:
            maxx = roll[number]
            res = number
        if roll[number] == maxx and number < res:
            res = number
    print(res)

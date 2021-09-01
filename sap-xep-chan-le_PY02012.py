n = int(input())
store = []
while True:
    tmp = list(map(int, input().split()))
    store += tmp
    if len(store) == n:
        break
chan, le = [], []
for i in store:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)
chan, le = sorted(chan), sorted(le)
indexChan, indexLe = 0, len(le)-1
for i in store:
    if i % 2 == 0:
        print(chan[indexChan], end=' ')
        indexChan += 1
    else:
        print(le[indexLe], end=' ')
        indexLe -= 1
print()

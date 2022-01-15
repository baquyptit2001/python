s = ""

for _ in range(int(input())):
    s += input() + " "

store = s.split()
sett = set(store)

dct = {}

for i in sett:
    dct[i] = round(store.count(i) / len(store), 2)

dct = sorted(dct.items(), key=lambda x: (-x[1], x[0]))

for i in dct:
    print("{} {:.2f}".format(i[0], i[1]))

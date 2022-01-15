s = ""

for _ in range(int(input())):
    s += input() + " "

store = s.split()
sett = set(store)

dct = {}

for i in sett:
    dct[i] = store.count(i)

dct = sorted(dct.items(), key=lambda x: (-x[1], x[0]))

mark = dct[0][1]
for i in dct[1:]:
    if i[1] != mark:
        mark = i[1]
        break

for i in dct:
    if i[1] == mark:
        print(i[0], end=" ")

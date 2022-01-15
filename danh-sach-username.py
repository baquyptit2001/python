store = []

for _ in range(int(input())):
    name = input()
    store.append(name.lower())

store = set(store)
store = sorted(store)
for i in store:
    print(i)

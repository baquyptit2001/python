number = input()
n = len(number)
store = set()
for i in range(0, n - (n % 2), 2):
    store.add(int(number[i] + number[i + 1]))
store = sorted(store)
for i in store:
    print(i, end=' ')

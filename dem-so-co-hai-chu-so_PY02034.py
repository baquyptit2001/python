import collections

number = input()
n = len(number)
store = []
for i in range(0, n - (n % 2), 2):
    tmp = int(number[i] + number[i + 1])
    store.append(tmp)
counter = collections.Counter(store)
for i in counter:
    print(i, counter[i])

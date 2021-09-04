number = input()
n = len(number)
store = []
for i in range(0, n - (n % 2), 2):
    tmp = int(number[i] + number[i + 1])
    if tmp not in store:
        store.append(tmp)
for i in store:
    print(i, end=' ')

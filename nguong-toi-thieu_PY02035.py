number = input()
k = int(input())
n = len(number)
mark = [0] * 100
store = []
unique = []
for i in range(0, n - (n % 2), 2):
    tmp = int(number[i] + number[i + 1])
    store.append(tmp)
    if tmp not in unique:
        unique.append(tmp)
    mark[tmp] += 1
unique.sort()
found = False
for i in unique:
    if mark[i] >= k:
        print(i, mark[i])
        found = True
if not found:
    print("NOT FOUND")

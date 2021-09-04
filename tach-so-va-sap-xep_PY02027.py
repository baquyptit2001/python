n = int(input())

store = []
for i in range(n):
    store.append(input())
numbers = []
for i in store:
    tmp = ''
    for j in range(len(i)):
        if i[j].isdigit():
            tmp += i[j]
        if (j == len(i) - 1 or not i[j + 1].isdigit()) and tmp != '':
            numbers.append(int(tmp))
            tmp = ''
numbers.sort()
for i in numbers:
    print(i)

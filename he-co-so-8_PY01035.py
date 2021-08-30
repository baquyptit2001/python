string = input()
while len(string) % 3 != 0:
    string = '0'+string
store, count, tmp = [], 0, ''
for i in string[::-1]:
    tmp += i
    count += 1
    if count == 3:
        store.append(tmp[::-1])
        tmp = ''
        count = 0
res = ''
for i in store:
    number = int(i, 2)
    res += str(number)
print(res[::-1])

t = int(input())

for u in range(t):
    raw_string = input()
    find = input()
    count = 0
    while raw_string.find(find) != -1:
        raw_string = raw_string.replace(find, '', 1)
        count += 1
    print(count)

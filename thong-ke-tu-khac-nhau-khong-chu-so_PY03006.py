import collections



t = int(input())

store = []
for u in range(t):
    string = input()
    for i in string:
        if (not i.isnumeric()) and (not i.isalpha()) and i != ' ':
            string = string.replace(i, ' ')
    string = string.lower()
    store += string.split(' ')
word_count = collections.Counter(store)
word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
for i in word_count:
    i = list(i)
    i[0] = ''.join([j for j in i[0] if not j.isdigit()])
    if i[0] != '':
        print(i[0], i[1])

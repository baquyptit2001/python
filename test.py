t = int(input())

for u in range(t):
    number = input()
    tmp = list(number)
    more, semi, up = False, False, False
    for i in range(len(tmp) - 1, 0, -1):
        if int(tmp[i]) < 5:
            tmp = list(number)
            if int(tmp[i]) < 5:
                tmp[i] = '0'
                continue
            else:
                tmp[i] = '0'
                if tmp[i - 1] != '9':
                    tmp[i - 1] = int(tmp[i - 1] + 1)
                    continue
                while tmp[i - 1] == '9':
                    tmp[i - 1] = '0'
                    tmp = list(number)
                    if tmp[i - 1] != '9':
                        tmp[i - 1] += 1
                        break
                    i -= 1
                    if i == 1 and tmp[0] != '9':
                        break
                    if i == 1 and tmp[0] == '9':
                        more = True
                        break
    if more:
        tmp.insert(0, '1')
    elif int(tmp[1]) >= 5:
        tmp[0] = str(int(tmp[0]) + 1)
    print(''.join(tmp))

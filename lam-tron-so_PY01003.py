t = int(input())
while t > 0:
    s = input()
    s = s[::-1]
    l = len(s)
    tmp = []
    for i in range(l):
        tmp.append(s[i])
    if l == 1:
        print(s)
    else:
        for i in range(len(tmp) - 1):
            if int(tmp[i]) >= 5:
                tmp[i] = '0'
                tmp[i + 1] = str(int(tmp[i + 1]) + 1)
            else:
                tmp[i] = '0'
        print(''.join(tmp[::-1]))
    t -= 1

t = int(input())

for u in range(t):
    s = list(str(i) for i in input())
    if len(s) == 1:
        print(-1)
        continue
    i = len(s) - 2
    while i >= 0 and s[i] <= s[i + 1]:
        i = i - 1
    if i < 0:
        print(-1)
    else:
        compare = i + 1
        for j in range(i + 1, len(s)):
            if s[i] > s[j] > s[compare]:
                compare = j
        s[compare], s[i] = s[i], s[compare]
        if s[0] == '0':
            print(-1)
        else:
            for j in s:
                print(j, end='')
            print()

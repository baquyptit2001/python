for _ in range(int(input())):
    s = input()
    find = input()
    res = 0
    while s.find(find) != -1:
        s = s[:s.find(find)] + s[s.find(find) + len(find):]
        res += 1
    print(res)

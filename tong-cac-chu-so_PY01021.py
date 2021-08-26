t = int(input())

for u in range(t):
    tong = 0
    string = input()
    result = ''
    for i in string:
        if i.isdigit():
            tong += int(i)
        else:
            result += i
    result = sorted(result)
    result = ''.join(result)
    print(result+str(tong))

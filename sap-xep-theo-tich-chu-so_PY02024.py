def sumNum(n):
    n = int(n)
    sum = 1
    while n != 0:
        sum *= n % 10
        n //= 10
    return sum


t = int(input())

while t > 0:
    n = int(input())
    listNum = list(map(int, input().split()))[:n]
    tmp = []
    for i in listNum:
        tmp.append([sumNum(i), i])
    tmp.sort()
    for i in range(0, len(tmp)):
        print(tmp[i][1], end=' ')
    print('')
    t -= 1
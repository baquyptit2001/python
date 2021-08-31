import math

n, x = [int(i) for i in input().split()]
nguyenTo = [0]
k, start = n, 2
while k > 0:
    flag = True
    for i in range(2, math.isqrt(start) + 1):
        if start % i == 0:
            flag = False
            break
    if (flag):
        nguyenTo.append(start)
        k -= 1
    start += 1
for i in nguyenTo:
    x += i
    print(x, end=' ')

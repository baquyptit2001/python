example = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

t = int(input())
for u in range(t):
    number, k = map(int, input().split())
    res = ''
    while (number > 0):
        r = number % k
        res = example[r] + res
        number = int(number / k)
    print(res)

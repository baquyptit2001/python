t = int(input())

for u in range(t):
    res = 1
    number = input()
    for i in number:
        if int(i) != 0:
            res *= int(i)
    print(res)

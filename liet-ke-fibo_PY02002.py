def init(fibo):
    for i in range(2, 94, 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])


fibo = [1, 1]
init(fibo)
t = int(input())

for u in range(t):
    a, b = [int(x) for x in input().split()]
    for i in range(a - 1, b, 1):
        print(fibo[i], end=' ')
    print()

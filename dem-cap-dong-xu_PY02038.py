import math

n = int(input())

store = []
for i in range(n):
    tmp = input()
    store.append(tmp)
res = 0
for i in store:
    coin = 0
    for j in i:
        if j == 'C':
            coin += 1
    if coin > 1:
        res += math.comb(coin, 2)
for i in range(n):
    coin = 0
    for j in range(n):
        if store[j][i] == 'C':
            coin += 1
    if coin > 1:
        res += math.comb(coin, 2)
print(res)

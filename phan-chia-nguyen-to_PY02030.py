import math


def nguyen_to(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1


n = int(input())
store = list(map(int, input().split()))
mark = {}
tmp = []
for i in store:
    if i not in mark:
        mark[i] = 1
        if len(tmp) == 0:
            tmp.append(i)
        else:
            tmp.append(i + tmp[-1])
res = -1
for i in range(0, len(tmp)):
    if nguyen_to(tmp[i]) and nguyen_to(tmp[-1] - tmp[i]):
        res = i
        break
if res == -1:
    print("NOT FOUND")
else:
    print(res)

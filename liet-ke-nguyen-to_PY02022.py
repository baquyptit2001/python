from math import isqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1, 1):
        if n % i == 0:
            return False
    return True


n = int(input())
store = list(map(int, input().split()))
number, count = [], []
for i in store:
    if prime(i):
        if i in number:
            count[number.index(i)] += 1
        else:
            number.append(i)
            count.append(1)
for i in range(len(number)):
    print(number[i], count[i])

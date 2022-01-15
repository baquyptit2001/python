def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


input()

store = [int(x) for x in input().split()]

store = sorted(store)

for i in range(len(store)):
    for j in range(i + 1, len(store)):
        if gcd(store[i], store[j]) == 1:
            print(store[i], store[j])

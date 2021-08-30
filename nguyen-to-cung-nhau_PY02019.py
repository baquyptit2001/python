def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n = int(input())
store = list(map(int, input().split()))
store = sorted(store)
for i in range(0, n - 1, 1):
    for j in range(i + 1, n, 1):
        if gcd(store[i], store[j]) == 1:
            print(store[i], store[j])

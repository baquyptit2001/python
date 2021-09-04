def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


n = int(input())

store = list(map(int, input().split()))
prime = []
for i in store:
    if is_prime(i):
        prime.append(i)
prime.sort()
count = 0
for i in store:
    if i in prime:
        print(prime[count], end=' ')
        count += 1
    else:
        print(i, end=' ')

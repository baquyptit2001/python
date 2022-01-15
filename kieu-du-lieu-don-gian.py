def sum_of_factor(n):
    sum = 0
    for i in range(2, n + 1):
        while n % i == 0:
            sum += i
            n /= i
    return sum


res = 1

t = int(input())

for i in range(t):
    n = int(input())
    res *= sum_of_factor(n)

print(res)

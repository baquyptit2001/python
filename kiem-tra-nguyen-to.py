import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    number = input()[-4:]
    if is_prime(int(number)):
        print("YES")
    else:
        print("NO")

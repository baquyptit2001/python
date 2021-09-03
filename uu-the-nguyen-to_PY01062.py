from math import isqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1, 1):
        if x % i == 0:
            return False
    return True


t = int(input())
check_digit = [2, 3, 5, 7]

for u in range(t):
    number = input()
    prime, non_prime = 0, 0
    for i in number:
        if int(i) in check_digit:
            prime += 1
        else:
            non_prime += 1
    if prime > non_prime and is_prime(len(number)):
        print("YES")
    else:
        print("NO")

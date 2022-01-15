from math import sqrt


def is_prime(n):
    flag = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag


def is_achilles_number(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if n % (i ** 2) == 0:
                continue
            return False
    return True


def is_perfect_number(n):
    sum = 0
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            sum += i
    return sum == n


num = int(input())

if is_prime(num):
    print(0)
else:
    if is_achilles_number(num) and not is_perfect_number(num):
        print(1)
    else:
        print(0)

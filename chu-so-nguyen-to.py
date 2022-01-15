def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def chu_so_nguyen_to(n):
    count = 0
    if not is_prime(len(n)):
        return "NO"
    for i in range(len(n)):
        if not is_prime(int(n[i])):
            count -= 1
        else:
            count += 1
    if count > 0:
        return "YES"
    else:
        return "NO"


for _ in range(int(input())):
    n = input()
    print(chu_so_nguyen_to(n))

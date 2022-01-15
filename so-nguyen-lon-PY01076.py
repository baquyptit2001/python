def gcd_big_number(a, b):
    if a == 0:
        return b
    return gcd_big_number(b % a, a)


t = int(input())
for _ in range(t):
    a = int(input())
    b = int(input())
    print(gcd_big_number(a, b))

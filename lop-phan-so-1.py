def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a, b = [int(x) for x in input().split()]
g = gcd(a, b)
print("{}/{}".format(a // g, b // g))

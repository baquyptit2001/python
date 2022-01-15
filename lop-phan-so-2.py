def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a, b, c, d = [int(x) for x in input().split()]
m = a * d + b * c
t = b * d
g = gcd(m, t)
print("{}/{}".format(m // g, t // g))

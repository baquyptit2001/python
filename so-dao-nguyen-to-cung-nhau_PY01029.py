def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


t = int(input())

for u in range(t):
    number = input()
    number, revNumber = int(number), int(number[::-1])
    if gcd(number, revNumber) == 1:
        print("YES")
    else:
        print("NO")

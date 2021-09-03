import math


def nguyenTo(n):
    if (n < 2):
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())

for u in range(t):
    number = input()
    num1 = number[0] + number[1] + number[2]
    num2 = number[len(number) - 1 - 2] + number[len(number) - 1 - 1] + number[len(number) - 1]
    if nguyenTo(int(num1)) and nguyenTo(int(num2)):
        print("YES")
    else:
        print("NO")

a, b, c = [int(x) for x in input().split()]
number = 0
if a % c == 0:
    number = a + b
else:
    number = b - (a % b)
if a + number > c:
    print("-1")
else:
    for i in range(number, c - a + 1, b):
        print(i, end=" ")

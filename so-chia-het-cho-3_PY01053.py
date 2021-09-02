t = int(input())

for u in range(t):
    number = input()
    sumDigit = 0
    for i in number:
        sumDigit += int(i)
    if sumDigit % 3 == 0:
        print("YES")
    else:
        print("NO")

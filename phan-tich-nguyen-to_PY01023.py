t = int(input())

for u in range(t):
    number = int(input())
    print(1, end=' ')
    for i in range(2, number + 1, 1):
        count = 0
        while number % i == 0:
            count += 1
            number /= i
        if count > 0:
            print("* {}^{} ".format(i, count), end=' ')
    print()

number = input()

while len(number) > 1:
    n = len(number)
    n1 = number[:n // 2]
    n2 = number[n // 2:]
    number = str(int(n1) + int(n2))
    print(number)

while True:
    n = int(input())
    if n == 0:
        break
    max = min = int(input())
    for u in range(n - 1):
        tmp = int(input())
        if tmp > max:
            max = tmp
        elif tmp < min:
            min = tmp
    if max == min:
        print("BANG NHAU")
    else:
        print(min, max)

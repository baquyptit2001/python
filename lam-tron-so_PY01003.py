t = int(input())

for u in range(t):
    if (int(number) < 10):
        print(number)
        continue
    number = input()
    tmp = list(number)
    for i in range(len(tmp) - 1, 0, - 1):


def checker(n):
    if len(n) % 2 != 0:
        return False
    for i in range(0, len(n) // 2, 1):
        if n[i] != n[len(n) - 1 - i] or int(n[i]) % 2 != 0:
            return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    for i in range(22, n, 2):
        if checker(str(i)):
            print(i, end=' ')
    print()



#x, y = [int(x) for x in [x, y]]
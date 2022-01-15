def check():
    for i in range(n):
        if a[i] > b[i]:
            return "NO"
    return "YES"


for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    print(check())

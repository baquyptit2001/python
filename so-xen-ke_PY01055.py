def checker(n):
    if len(n) % 2 == 0:
        return "NO"
    if n[0] == n[1]:
        return "NO"
    compare = n[0]
    for i in range(2, len(n), 2):
        if n[i] != compare:
            return "NO"
    return "YES"


t = int(input())

for u in range(t):
    number = input()
    print(checker(number))

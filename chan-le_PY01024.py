def checker(s):
    digs = int(s[0])
    for i in range(1, len(s), 1):
        digs += int(s[i])
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            return "NO"
    if digs % 10 == 0:
        return "YES"
    return "NO"


t = int(input())

for u in range(t):
    string = input()
    print(checker(string))

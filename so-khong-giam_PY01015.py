def checker(s):
    for i in range(1, len(s), 1):
        if int(s[i]) < int(s[i - 1]):
            return "NO"
    return "YES"


t = int(input())

for u in range(t):
    string = input()
    print(checker(string))

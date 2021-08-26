def checker(s):
    for i in s:
        if i != '4' and i != '7':
            return "NO"
    return "YES"


t = int(input())

for u in range(t):
    string = input()
    print(checker(string))

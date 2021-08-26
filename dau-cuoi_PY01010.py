def checker(s):
    s1, s2 = s[0] + s[1], s[-2] + s[-1]
    if s1 == s2:
        return "YES"
    return "NO"


t = int(input())

for u in range(t):
    string = input()
    print(checker(string))

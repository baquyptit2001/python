def check(s):
    checker = s[len(s)-2]+s[len(s)-1]
    if checker == "86":
        return "YES"
    return "NO"


t = int(input())
for u in range(t):
    string = input()
    print(check(string))

t = int(input())

for u in range(t):
    string1 = input()
    string2 = input()
    if len(string1) != len(string2):
        print("Test {}: {}".format(u + 1, "NO"))
        continue
    res = "NO"
    if sorted(string1) == sorted(string2):
        res = "YES"
    print("Test {}: {}".format(u+1, res))

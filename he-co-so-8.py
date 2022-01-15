string = input()

res = ""
while len(string) > 3:
    res = str(int(string[-3:], 2)) + res
    string = string[:-3]
if len(string) > 0:
    res = str(int(string[-3:], 2)) + res
print(res)

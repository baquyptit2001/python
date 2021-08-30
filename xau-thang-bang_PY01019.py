t = int(input())

for u in range(t):
    string = input()
    string2 = string[::-1]
    res = "YES"
    for i in range(1, len(string)):
        if abs(ord(string[i])-ord(string[i-1]))!=abs(ord(string2[i])-ord(string2[i-1])):
            res="NO"
            break
    print(res)
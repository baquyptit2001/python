t = int(input())
example = ''
for i in range(65, 91):
    example += chr(i)
for u in range(t):
    string = input()
    n = len(string)
    s1 = string[:n // 2]
    s2 = string[n // 2:]
    s1 = list(s1)
    s2 = list(s2)
    x1, x2 = 0, 0
    for i in range(len(s1)):
        x1 += ord(s1[i])
        x2 += ord(s2[i])
    for i in range(len(s1)):
        s1[i] = example[(x1 + ord(s1[i]) - ord('A')) % 26]
        s2[i] = example[(x2 + ord(s2[i]) - ord('A')) % 26]
    for i in range(len(s1)):
        s1[i] = example[(ord(s1[i]) + ord(s2[i]) - 2 * ord('A'))%26]
    s1 = ''.join(s1)
    print(s1)

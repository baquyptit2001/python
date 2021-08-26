t = int(input())

for u in range(t):
    string = input()
    result, count = "", 0
    for i in range(len(string)):
        count += 1
        if i == (len(string) - 1) or string[i] != string[i + 1]:
            result += str(count) + string[i]
            count = 0
    print(result)

def check(num):
    if len(num) < 3:
        return "NO"
    inc = True
    if num[0] > num[1] or num[1] == num[0]:
        return "NO"
    for i in range(2, len(num)):
        if num[i] == num[i-1]:
            return "NO"
        if inc:
            if num[i] < num[i - 1]:
                inc = False
        else:
            if num[i] > num[i - 1]:
                return "NO"
    if not inc:
        return "YES"


for _ in range(int(input())):
    num = input()
    print(check(num))

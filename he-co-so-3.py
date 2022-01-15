def check():
    for i in number:
        if not (i == '0' or i == '1' or i == '2'):
            return "NO"
    return "YES"


for _ in range(int(input())):
    number = input()
    print(check())

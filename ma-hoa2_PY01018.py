example = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    string = input()
    if string == "0":
        break
    num, code = string.split()
    num = int(num)
    result = ""
    for i in code:
        result += example[(example.index(i)+num) % 28]
    print(result[::-1])

result = []
store = []
while True:
    string = input()
    string = string.split()
    for i in string:
        store.append(int(i))
    for i in store:
        if (i % 42) not in result:
            result.append(i % 42)
    if len(store) == 10:
        print(len(result))
        break
    a = "YES" if True else "NO"

for _ in range(int(input())):
    string = input()
    store = []
    tmp = ""
    for i in string:
        if i.isnumeric():
            tmp += i
        elif not i.isnumeric() and tmp != "":
            store.append(int(tmp))
            tmp = ""
    if tmp != "":
        store.append(int(tmp))
    print(max(store))

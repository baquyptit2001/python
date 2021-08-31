while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
        continue
    store = set()
    store.add(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
            store.add(n)
        else:
            n = n * 3 + 1
            store.add(n)
    print(len(store))

while True:
    store = [int(x) for x in input().split()]
    if store[0] == store[1] == store[2] == store[3] == 0:
        break
    tmp, count = [0] * 4, 0
    while True:
        if store[0] == store[1] == store[2] == store[3]:
            break
        count += 1
        store[0], store[1], store[2], store[3] = abs(store[0] - store[1]), abs(store[1] - store[2]), abs(
            store[2] - store[3]), abs(store[0] - store[3])
    print(count)

def cal_sum(old, new):
    consume = new - old
    if consume <= 50:
        res = consume * 100 * 102 / 100
        return res
    else:
        res = 50 * 100
        consume -= 50
    if consume <= 50:
        res += consume * 150
        return res * 103 / 100
    else:
        res += 50 * 150
        consume -= 50
    res += consume * 200
    return res * 105 / 100


class Customer:
    def __init__(self, code, name, old, new):
        self.code = "KH" + code.zfill(2)
        self.name = name
        self.consumption = cal_sum(old, new)


store = []
for _ in range(int(input())):
    name = input()
    old = int(input())
    new = int(input())
    store.append(Customer(str(len(store) + 1), name, old, new))
    store.sort(key=lambda x: x.consumption, reverse=True)
for i in store:
    print(i.code, i.name, int(round(i.consumption)))

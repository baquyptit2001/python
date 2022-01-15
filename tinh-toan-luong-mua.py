class Mua:
    def __init__(self, code, loca, t_in, t_out, mua):
        self.code = "T" + code.zfill(2)
        time = [int(x) for x in t_in.split(":")]
        self.time = time[0] * 60 + time[1]
        time = [int(x) for x in t_out.split(":")]
        self.time = time[0] * 60 + time[1] - self.time
        self.loca = loca
        self.mua = mua


count = 1
store = []
for _ in range(int(input())):
    loca = input()
    t_in = input()
    t_out = input()
    mua = int(input())
    if len(store) == 0:
        store.append(Mua(str(count), loca, t_in, t_out, mua))
        count += 1
        continue
    found = False
    for i in store:
        if i.loca == loca:
            time = [int(x) for x in t_in.split(":")]
            timee = time[0] * 60 + time[1]
            time = [int(x) for x in t_out.split(":")]
            timee = time[0] * 60 + time[1] - timee
            i.time += timee
            i.mua += mua
            found = True
            break
    if not found:
        store.append(Mua(str(count), loca, t_in, t_out, mua))
        count += 1
for i in store:
    print("{} {} {:.2f}".format(i.code, i.loca, round(i.mua / i.time * 60, 2)))

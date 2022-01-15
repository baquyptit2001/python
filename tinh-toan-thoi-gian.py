class Player:
    def __init__(self, name, code, t_in, t_out):
        self.name = name
        self.code = code
        time = [int(x) for x in t_in.split(':')]
        self.time = time[0] * 60 + time[1]
        time = [int(x) for x in t_out.split(':')]
        self.time = time[0] * 60 + time[1] - self.time


player = []

for _ in range(int(input())):
    code = input()
    name = input()
    t_in = input()
    t_out = input()
    player.append(Player(name, code, t_in, t_out))

player.sort(key=lambda x: x.time, reverse=True)

for i in player:
    print("{} {} {} gio {} phut".format(i.code, i.name, i.time // 60, i.time % 60))

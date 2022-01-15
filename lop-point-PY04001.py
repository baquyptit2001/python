from math import sqrt


class Point:
    def __init__(self, x1, y1, x2, y2):
        self.a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def distance(self):
        return self.a


if __name__ == "__main__":
    t = int(input())
    for u in range(t):
        x1, y1, x2, y2 = map(int, input().split())
        p = Point(x1, y1, x2, y2)
        print('{:.4f}'.format(p.distance()))

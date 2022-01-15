class Rectangle:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def color(self):
        return self.colour.title()


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
if int(arr[0]) > 0 and int(arr[1]) > 0:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")

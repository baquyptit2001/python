class Student:
    def __init__(self, code, name, score):
        self.code = 'HS' + code.zfill(2)
        self.name = name
        self.score = round((score[0] * 2 + score[1] * 2 + score[2] + score[3] + score[4] + score[5] + score[6] + score[
            7] + score[8] + score[9] + 0.01) / 12, 1)
        self.title = "YEU"
        if self.score >= 5:
            self.title = "TB"
        if self.score >= 7:
            self.title = "KHA"
        if self.score >= 8:
            self.title = "GIOI"
        if self.score >= 9:
            self.title = "XUAT SAC"


def mixed_order(a):
    return -a.score, a.code


students = []
for i in range(int(input())):
    name = input()
    code = i + 1
    score = list(map(float, input().split()))
    students.append(Student(str(code), name, score))
students.sort(key=mixed_order)
for i in students:
    print(i.code, i.name, i.score, i.title)

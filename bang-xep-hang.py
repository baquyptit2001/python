class Student:
    def __init__(self, name, score, submit):
        self.name = name
        self.score = score
        self.submit = submit


def order(a):
    return -a.score, a.submit, a.name


students = []
for _ in range(int(input())):
    name = input()
    score, submit = map(int, input().split())
    students.append(Student(name, score, submit))

students.sort(key=order)

for i in students:
    print(i.name, i.score, i.submit)
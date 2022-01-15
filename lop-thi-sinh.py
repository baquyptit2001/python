class Student:
    def __init__(self, name, age, score1, score2, score3):
        self.name = name
        self.age = age
        self.score = score1 + score2 + score3


if __name__ == "__main__":
    name = input()
    age = input()
    score1 = float(input())
    score2 = float(input())
    score3 = float(input())
    student = Student(name, age, score1, score2, score3)
    print("{} {} {:.1f}".format(student.name, student.age, student.score))

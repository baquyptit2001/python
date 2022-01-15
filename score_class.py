name = input()
score1 = int(input())
score2 = int(input())
score3 = int(input())

print("{} {:.1f}".format(name, round((score1 + score2*3 + score3*6) / 10, 1)))

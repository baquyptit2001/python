def thuanNghich(n):
    if len(n) == 1:
        return "NO"
    for i in range(0, len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
            return "NO"
    return "YES"


t = int(input())

for u in range(t):
    number = input()
    sumDigit = 0
    for i in number:
        sumDigit += int(i)
    print(thuanNghich(str(sumDigit)))

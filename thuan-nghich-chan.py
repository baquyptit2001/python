def make(n):
    num = str(n)
    return num + num[::-1]


def check(n, com):
    if int(make(n)) > com:
        return False
    return True


def isPowerOfTen(n):
    return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0


first = [22, 44, 66, 88]
for _ in range(int(input())):
    num = int(input())
    for i in first:
        if i < num:
            print(i)
    start = 2
    after = 0
    num_of = 1
    while check(make(str(start) + str(after).zfill(num_of)), num):
        print(make(str(start) + str(after).zfill(num_of)))
        after += 1
        if isPowerOfTen(after):
            after = 0
            num_of += 1
            start += 2
        else:
            after += 1
        if start == 8:
            start = 2
        else:
            start += 2


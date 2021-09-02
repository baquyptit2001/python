def digitSum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


number = input()
count = 0
sum = 0
if len(number) > 1:
    for i in number:
        sum += (ord(i)-ord('0'))
    count += 1
    number = sum
    count = 1
    if number >= 10:
        while True:
            count += 1
            number = digitSum(number)
            if number < 10:
                break
print(count)

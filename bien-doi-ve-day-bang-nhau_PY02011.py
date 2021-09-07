n = int(input())
a = list(map(int, input().split()))
compare = 10 ** 9
res = 0
for i in a:
    count = 0
    for j in a:
        count += abs(j - i)
    if count < compare:
        compare = count
        res = i
print(compare, res)

n, m = [int(x) for x in input().split()]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = set(a)
b = set(b)
common, AminusB, BminusA = [], [], []
a, b = sorted(a), sorted(b)
for i in a:
    if i in b:
        common.append(i)
    else:
        AminusB.append(i)
for i in b:
    if i not in common and i not in BminusA:
        BminusA.append(i)
for i in common:
    print(i, end=' ')
if len(common) > 0:
    print()
for i in AminusB:
    print(i, end=' ')
if len(AminusB) > 0:
    print()
for i in BminusA:
    print(i, end=' ')
print()
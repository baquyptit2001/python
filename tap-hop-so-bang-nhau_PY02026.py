n, m = [int(x) for x in input().split()]

A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = set(A)
b = set(B)
if len(a.difference(b)) == 0 and len(b.difference(a)) == 0:
    print("YES")
else:
    print("NO")

s1 = input().lower()
s2 = input().lower()

common = sorted(set(s1.split()) & set(s2.split()))
diff = sorted(set(s1.split()) | set(s2.split()))

for i in diff:
    print(i, end=' ')
print()
for i in common:
    print(i, end=' ')

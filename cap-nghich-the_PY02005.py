n = int(input())
store = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if store[i] > store[j]:
            count += 1
print(count)

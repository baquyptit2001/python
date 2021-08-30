n = int(input())
res = 0
store = list(map(int, input().split()))
store = sorted(store)
for i in range(1, n):
    if store[i]-store[i-1]!=1:
        res=store[i-1]+1
        break
if res==0:
    res=store[n-1]+1
print(res)
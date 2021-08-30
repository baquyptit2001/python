t = int(input())

for u in range(t):
    n, x, m = [float(x) for x in input().split()] 
    res = 0
    while n<m:
        n=n+n*(x/100)
        res+=1
    print(res)
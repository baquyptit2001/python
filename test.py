def isThuanNghich(n):
    for i in range(0, len(n)//2, 1):
        if n[i] != n[len(n)-1-i]:
            return False
    return True


t=int(input())
for i in range(t):
       n=int(input())
       for i in range(22,n,2):
           if isThuanNghich(str(i)):
               print(i,end=' ')
       print()
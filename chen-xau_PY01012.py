s1 = input()
s2 = input()
position = int(input())
if position == len(s1)+1:
    print(s1+s2)
else:
    for i in range(0, len(s1), 1):
        if i+1 == position:
            print(s2, end='')
        print(s1[i], end='')

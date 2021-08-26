string = input()
amount = 0
for i in string:
    if i == '4' or i == '7':
        amount += 1
    if amount > 7:
        break
if amount == 4 or amount == 7:
    print("YES")
else:
    print("NO")

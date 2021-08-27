def tong(a, b):
    if len(a) != len(b):
        b = '0' * (len(a) - len(b)) + b
    a, b = a[::-1], b[::-1]
    du, res = 0, ''
    l = len(a)
    for i in range(l):
        cong = int(a[i]) + int(b[i]) + int(du)
        res += str(cong % 10)
        du = int(cong // 10)
    if du != 0:
        res += '1'
    return res[::-1]


a = input()
b = input()
a = a.lstrip('0')
b = b.lstrip('0')
if a == '0' * len(a) and b == '0' * len(b):
    print("0")
else:
    if len(b) > len(a):
        a, b = b, a
    res = tong(a, b)
    res = res.lstrip('0')
    print(res)

import re


def check(password):
    if len(password) < 6 or len(password) > 12:
        return False
    elif not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not re.search("[$#@]", password):
        return False
    return True


for _ in range(int(input())):
    res = []
    store = input().split(',')
    for i in store:
        if check(i):
            res.append(i)
    print(','.join(res))

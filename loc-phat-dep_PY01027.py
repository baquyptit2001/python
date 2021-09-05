def checker(string):
    n = len(string)
    for i in range(n):
        if string[i] == '6':
            continue
        if string[i] != '8' and string[i] != '6':
            return "NO"
        if string[i] == '8':
            if (i == 0 or string[i - 1] != '6') and (i < 2 or (string[i - 1] != '8' or string[i - 2] != '6')):
                return "NO"
    return "YES"


string_input = input()
print(checker(string_input))

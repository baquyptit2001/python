from itertools import permutations

string = input()

res = list(permutations(string, len(string)))

for i in res:
    print(''.join(i))

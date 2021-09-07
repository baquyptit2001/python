import collections

m, n = [int(x) for x in input().split()]

vote_result = list(map(int, input().split()))

vote_count = collections.Counter(vote_result)
vote_count = sorted(vote_count.items(), key=lambda item: (-item[1], item[0]))
compare = vote_count[0][1]
found = False
for i in vote_count:
    if i[1] != compare:
        print(i[0])
        found = True
        break
if not found:
    print("NONE")

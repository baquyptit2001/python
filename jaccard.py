import math


def jac_card(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    inter = set1.intersection(set2)
    union = set1.union(set2)
    jaccard = len(inter) / len(union)
    return jaccard


def haversine_distance(lat1, lon1, lat2, lon2):
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    a = (delta_lat / 2) ** 2 + (delta_lon / 2) ** 2
    c = 2 * math.sin(math.sqrt(a))
    return c


lon1, lat1 = [float(x) for x in input().split()]
lon2, lat2 = [float(x) for x in input().split()]

print(round(haversine_distance(lat1, lon1, lat2, lon2), 3))

# s1 = input().lower().split()
# s2 = input().lower().split()
# s1 = list(''.join(s1))
# s2 = list(''.join(s2))
#
# print(round(jac_card(s1, s2), 2))

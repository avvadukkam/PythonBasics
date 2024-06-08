# Brute Force
def mat_prod(test_list):
    prod = 1
    for ele in test_list:
        for x in ele:
            prod *= x
    return prod


test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
print(mat_prod(test_list))


# Using list comprehension + loop
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


test_list1 = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
res = prod([ele for sub in test_list1 for ele in sub])
print(res)

#Using chain() + loop
from itertools import chain
def prod1(val1):
    res1 = 1
    for ele1 in val1:
        res1 *= ele1
    return res1
test_list2 = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
res1 = prod(list(chain(*test_list2)))
print(res1)
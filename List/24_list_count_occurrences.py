# Brute force
def countX(lst, x):
    count = 0
    for ele in lst:
        if(ele == x):
            count += 1
    return count


lst = [15, 6, 7, 10, 12, 10, 28, 10]
x = 10
print("{} has occurred {} times".format(x, countX(lst, x)))

# Using count()
def countY(lst1, y):
    return lst1.count(y)

lst1 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
y = 8
print("{} has occurred {} times".format(y, countY(lst1, y)))

# Using counter()
from collections import Counter
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

z = 3
d = Counter(l)
print("{} has occurred {} times".format(z, d[z]))

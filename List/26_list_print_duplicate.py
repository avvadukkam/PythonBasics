# Using Brute Force
def duplicate(x):
    repeated = []
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(duplicate(list1))

# Using Counter()
from collections import Counter
list2 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
d = Counter(list2)
print(d)
new_list = list([item for item in d if d[item]>1])
print(new_list)
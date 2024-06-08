# Brute Force
def merge(list1, list2):
    new_list = []
    for x in range(0, len(list2)):
        new_list.append((list2[x], list1[x]))
        new_list.sort()
    sorted_list = []
    for (l, m) in new_list:
        sorted_list.append(m)
    return sorted_list

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print(merge(list1, list2))

# zip()
def sort_list1(list3, list4):
    zipped_pairs = zip(list4,list3)
    z = [x for _, x in sorted(zipped_pairs)]
    return z

x = ["a","b","c","d","e","f","g","h","i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print(sort_list1(x,y))

# Using Dictionary, list comprehension, lambda fn
def sorting_of_element(l1,l2):
    f_1 = {}
    final_list = []
    f_1 = {l1[i]:l2[i] for i in range(len(l2))}
    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

    for i in f_lst.keys():
        final_list.append(i)
    return final_list

l1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
l2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
print(sorting_of_element(l1,l2))

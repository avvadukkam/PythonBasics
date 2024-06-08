def Cumulative(x):
    c_list = []
    y=0
    for i in range(len(x)):
        y += x[i]
        c_list.append(y)
    return c_list

list1 = [10, 20, 30, 40, 50]
print(Cumulative(list1))

# Using list comprehension
def Cumulative1(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]

lists = [10, 20, 30, 40, 50]
print(Cumulative1(lists))
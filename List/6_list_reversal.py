# brute force
def list_reversal(lst):
    i = len(lst)
    temp = []
    while i > 0:
        temp.append(lst.pop())
        i -= 1
    return temp
lst = [1, 2, 3, 4]
print(list_reversal(lst))


# using reversed()
def Reverse(lst1):
    return [ele for ele in reversed(lst1)]
lst1 = [10, 11, 12, 13, 14, 15]
print(Reverse(lst1))


# Using reverse()
def Reverse2(lst2):
    lst2.reverse()
    return lst2
lst2 = [1, 2, 3, 4, 5]
print(Reverse2(lst2))


# Using slicing
def Reverse3(lst3):
    new_lst = lst3[::-1]
    return new_lst
lst3 = [4, 5, 6, 7, 8, 9]
print(Reverse3(lst3))
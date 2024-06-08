# Using slicing
def Cloning(li1):
    li_copy = li1[:]
    return li_copy
li1 = [4, 8, 2, 10, 15, 18]
print("After Cloning li1 : ", Cloning(li1))

# Using extend() method
def Cloning2(li2):
    li2_copy = []
    li2_copy.extend(li2)
    return li2_copy
li2 = [14, 8, 21, 1, 5, 18]
print("After Cloning li2 : ", Cloning2(li2))

# Using list() method
def Cloning3(li3):
    li3_copy = list(li3)
    return li3_copy
li3 = [5, 6, 12, 3, 41, 32, 9]
print("After Cloning li3 : ", Cloning3(li3))

# Using list comprehension
def Cloning4(li4):
    li_copy = [i for i in li4]
    return li_copy

li4 = [4, 8, 2, 10, 15, 18]
li4_clone = Cloning4(li4)
print("Original List : ", li4)
print("Cloned List : ", li4_clone)

# Using append() method
def Cloning5(li5):
    li5_copy = []
    for item in li5: li5_copy.append(item)
    return  li5_copy

li5 = [4, 8, 2, 10, 15, 18]
print("After cloning : ", Cloning5(li5))

# Using copy() method
def Cloning6(li6):
    li6_copy = []
    li6_copy = li6.copy()
    return  li6_copy

li6 = [4, 8, 2, 10, 15, 18]
print("After Cloning : ", Cloning6(li6))
SS
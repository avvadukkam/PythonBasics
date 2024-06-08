# Using sort
list1 = [20, 10, 20, 4, 100]
list1.sort()
print("The largest value in the list is : ",list1[-1])

# Using max()
print("The largest value in the list is : ", max(list1))

# Brute Force
def myMax(list2):
    max = list2[0]
    for x in list2:
        if x>max:
            max = x
    return max
list2 = [10, 20, 4, 45, 99]
print("The largest element is : ", myMax(list2))
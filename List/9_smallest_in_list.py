# Using sort
list1 = [24, 5, 63]
list1.sort()
print("The smallest element is : ", list1[0])

# Using min()
print("The smallest element is : ", min(list1))

# Brute Force
l = [int(l) for l in input("List : ").split(",")]
print("The list is ",l)
min1 = l[0]
for i in range(len(l)):
    if l[i] < min1:
        min1 = l[i]
print("The smallest element in the list is ", min1)
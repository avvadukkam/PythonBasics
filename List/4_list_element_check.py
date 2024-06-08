from bisect import bisect_left, bisect

# Checking using loop
list1 = [1, 6, 3, 2, 5, 4]
list_bisect = list1
elem = 5
for i in list1:
    if (i == elem):
        print("Using loop : Element Exists")

# Using in
if (elem in list1):
    print("Using 'in' : Element Exists")

# Using set() + in

list1 = set(list1)
if elem in list1:
    print("Using set() + in : Element Exists")

# Using sort() + bisect_left()

list_bisect.sort()
if bisect_left(list_bisect, elem) != bisect(list_bisect, elem):
    print("Using sort() + bisect_left() : Element Exists")
else:
    print("Element doesn't exist")

# Using count()
test_list = [10, 15, 20, 7, 46, 2808]
print("\nChecking if 15 exist in list")
exist_count = test_list.count(15)
if exist_count >0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")
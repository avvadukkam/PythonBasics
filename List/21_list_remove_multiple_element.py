# Remove selected list
input_list = [12, 15, 3, 10]
remove_list = [12, 3]
for num in remove_list:
    if num in input_list:
        input_list.remove(num)
print(input_list)

# Remove elements divisible by 2
list1 = [11, 5, 17, 18, 23, 50]
for ele in list1:
    if ele % 2 ==0:
        list1.remove(ele)

print("New list after removing all even numbers: ", list1)

# Using list comprehension to remove even
list2 = [11, 5, 17, 18, 23, 50]
list2 = [elem for elem in list2 if elem % 2 != 0]
print(*list2)

# Remove elements by slicing
list3 = [11, 5, 17, 18, 23, 50]
del list3[1:5]
print(*list3)

# Using list comprehension
list4 = [11, 5, 17, 18, 23, 50]
unwanted_elem = {11, 5}
list4 = [ele for ele in list4 if ele not in unwanted_elem]
print("New list after removing unwanted number: ", list4)

# When the index of element is known
list5 = [11, 5, 17, 18, 23, 50]
unwanted = [0, 3, 4]
for ele in sorted(unwanted, reverse= True):
    del list5[ele]
print(*list5)
# Using for loop
lst = [12, -7, 5, 64, -14]
for num in lst:
    if num<0:
        lst.remove(num)
print(lst)

# Using while loop
list1 = [-10, 21, -4, -45, -66, 93]
num1 = 0
while(num1 < len(list1)):
    if list1[num1] >=0:
        print(list1[num1], end=" ")
    num1 += 1

# Using list comprehension
list2 = [-10, 21, -4, -45, -66, 93]
pos_nos = [num2 for num2 in list2 if num2 >=0]
print("\nPositive numbers in the list: ", *pos_nos)

# Using lambda expressions
list3 = [-10, 21, -4, -45, -66, 93, 11]
pos_nos1 = list(filter(lambda x:(x>=0), list3))
print("Positive numbers in the list: ", *pos_nos1)
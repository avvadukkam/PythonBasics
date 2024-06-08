# Using while loop
def odd_list(lst):
    temp_lst = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 1:
            temp_lst.append(lst[i])
        i += 1
    return temp_lst


lst = [54, 5, 7, 94, 58, 14]
print(odd_list(lst))

# Using for loop
list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
    if num % 2 != 0:
        print(num, end=" ")

# Using list comprehension:
list2 = [10, 21, 4, 45, 66, 93]
only_odd = [num1 for num1 in list2 if num1 % 2 == 1]
print("\nOdd number in the list2 = ",only_odd)

# Using lambda expression
list3 = [10, 21, 4, 45, 66, 93, 11]
odd_nos = list(filter(lambda x:(x%2!=0), list3))
print("Odd numbers in the list: ", odd_nos)
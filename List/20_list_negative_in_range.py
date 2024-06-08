start, end = -4, 5
lst = []
for num in range(start, end+1):
    if num <0:
        lst.append(num)

print("List of negative numbers is : ", *lst)
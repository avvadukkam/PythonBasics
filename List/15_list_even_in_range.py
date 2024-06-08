# Using for loop
start, end = 2, 15
lst = []
for num in range(start, end+1):
    if num%2 == 0:
        lst.append(num)
print(lst)

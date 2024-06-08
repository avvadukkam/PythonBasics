lst = [2, 4, -5, -6, 9, 2, 3, 7]
n = 4
lst.sort()
print(lst[-n:])

# Using Brute force or Selection Sort
lst1 = [2, 14, -15, -6, -9, 2, 3, -7]
i = 0
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i] >= lst1[j]:
            lst1[i], lst1[j] = lst1[j], lst1[i]
print(lst1[-3:])

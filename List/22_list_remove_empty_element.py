# Using list comprehension
test_list = [5, 6, [], 3, [], [], 9]
print("The original list : ", str(test_list))
res = [ele for ele in test_list if ele != []]
print("The list after removing empty list = ", res)

# Using filter()
test_list = [5, 6, [], 3, [], [], 9]
res1 = list(filter(None, test_list))
print("List after empty list removal : ", res1)

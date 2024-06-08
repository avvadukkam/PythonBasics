# Brute force for 2 digit
def digit_sum(list1):
    new_list = []
    for num in list1:
        sum =0
        sum = int(num/10)+num%10
        new_list.append(sum)
    return new_list

list1 = [12, 67, 98, 34]
print(digit_sum(list1))

# Using loop + str()
test_list = [12, 67, 98, 34]
res = []
for ele in test_list:
    sum1 = 0
    for digit in str(ele):
        sum1 += int(digit)
    res.append(sum1)
print(res)

# Using sum() + list comprehension
test_list2 = [12, 67, 98, 34]
res2 = list(map(lambda elem: sum(int(sub) for sub in str(elem)), test_list2))
print(res2)

# Using sum() + reduce()
from functools import reduce
test_list3 = [121, 67, 98, 34]
res3 = [reduce(lambda x, y: int(x) + int(y),list(str(i))) for i in test_list3]
print(res3)
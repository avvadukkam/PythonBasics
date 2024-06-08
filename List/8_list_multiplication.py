# Using Traversal
import math


def lst_mult(lst):
    prod = 1
    for value in lst:
        prod *= value
    return prod
lst = [1, 2, 3]
print("Product of all element = ", lst_mult(lst))

# Using numpy.prod()
import numpy
list1 = [3, 2, 4]
result1 = numpy.prod(list1)
print("Product of all element = ", result1)

# Using lambda fn and reduce()
from functools import reduce
list2 = [2,4,5]
result2 = reduce((lambda  x, y: x*y), list2)
print("Product of all element = ", result2)

# Using math.prod
import math
list3 = [1,4,7]
result3 = math.prod(list3)
print("Product of all element = ", result3)
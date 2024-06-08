def lst_sum(lst):
    sum = 0
    for value in lst:
        sum += value
    return sum


lst = [12, 15, 3, 10]
print("Sum of all element = ", lst_sum(lst))

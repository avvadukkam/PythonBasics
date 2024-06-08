def swapElement(list):
    n = len(list)
    temp = list[0]
    list[0] = list[n - 1]
    list[n - 1] = temp
    return list
list = [12, 35, 9, 56, 24]
print(swapElement(list))
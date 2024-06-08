def even_list(lst):
    temp_lst = []
    i = 0
    while i < len(lst):
        if lst[i]%2 == 0:
            temp_lst.append(lst[i])
        i += 1
    return temp_lst
lst = [54, 5, 7, 94, 58, 14]
print(even_list(lst))
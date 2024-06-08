def rotateArray(arr, d, n):
    tempArr = []
    i = 0
    while(i < d):
        tempArr.append(arr[i])
        i += 1
    i=0
    for i in range(0,len(tempArr)):
        arr.append(tempArr[i])
    arr[:]=arr[d:]
    return arr
    '''#simple solution
    return arr[d:n]+arr[:d]
    '''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rotateArray(arr, 4, len(arr)))

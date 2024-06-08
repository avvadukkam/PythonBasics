def splitArr(arr, n, d):
    tempArr1 = []
    tempArr2 = []
    for i in range(0,d):
        tempArr1.append(arr[i])
    for i in range(d,len(arr)):
        tempArr2.append(arr[i])
    arr = tempArr2 + tempArr1
    return arr

arr = [12,10,5,6,52,36]
print(splitArr(arr,len(arr),2))

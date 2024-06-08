def array_remainder(arr, n):
    prod = 1
    for i in range(0, len(arr)):
        prod *= arr[i]
    return prod % n


arr = [100, 10, 5, 25, 35, 14]
n = 11
print(array_remainder(arr, n))

def sum_array(arr):
    sum1 = 0
    for i in range(0, len(arr)):
        sum1 += arr[i]
    return sum1


arr = []
while True:
    s = input("Enter the number : ")
    if s == "q":
        break
    else:
        arr.append(float(s))
print("Array = ", arr)
print("The sum of elements in the array is = ", sum_array(arr))

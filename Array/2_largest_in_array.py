def largest(arr):
    max = arr[0]
    for i in range(1,n):
        if arr[i]>=max:
            max = arr[i]
    return arr[i]
arr = []
while True:
    s = input("Enter the number : ")
    if s == "q":
        break
    else:
        arr.append(float(s))
n = len(arr)
print("Array = ", arr)
print("The largest elements in the array is = ", largest(arr))

def rotation(arr1):
    n = len(arr1)-1
    while n>=0:
        arr2.append(arr1[n])
        n-=1
    return arr2
arr1 = []
arr2 = []
while True:
    s = input("Enter the number : ")
    if s == "q":
        break
    else:
        arr1.append(float(s))
print("Array = ", arr1)
print("Rotated Array = ", rotation(arr1))

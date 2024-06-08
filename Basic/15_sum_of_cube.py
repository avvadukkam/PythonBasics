def cubeSum(n):
    sum = 0
    for i in range(1,n+1):
        sum += pow(i,3)
    return sum
n = int(input("The value of N: "))
print("The sum of cube of first {} natural number is {}".format(n,cubeSum(n)))
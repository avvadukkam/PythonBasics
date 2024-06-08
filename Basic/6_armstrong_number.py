def isArmstrong(x):
    n = len(str(x))
    temp = x
    sum1 = 0
    while(temp != 0):
        r = temp % 10
        sum1 = sum1 + pow(r,n)
        temp = temp//10
    return (sum1 == x)
x = int(input("Enter the number to check : "))
print(isArmstrong(x))

# Using easy method
x = 153
sum = 0
for i in str(x):
    sum += pow(int(i),len(str(x)))
print(sum)

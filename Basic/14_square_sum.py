def square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i*i
    return sum
n = int(input("The value of N : "))
print("The sum of square of first {} natural numbers is {}".format(n,square_sum(n)))
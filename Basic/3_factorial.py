def factorial(n):
    return 1 if(n==0 or n==1) else n*factorial(n-1)
n=int(input("Type the number to find factorial : "))
print("{}! = {}".format(n,factorial(n)))
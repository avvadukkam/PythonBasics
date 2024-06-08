def isPrime(n):
    if n>1:
        for i in range(2, int(n/2)+1):
            if (n%i)==0:
                return False
                break
        else:
            return True
n = int(input("Enter the number to check: "))
if isPrime(n)==True:
    print("The number {} is prime".format(n))
else:
    print("The number {} is not prime".format(n))

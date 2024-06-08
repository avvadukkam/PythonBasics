def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 3
    while i!=0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if (f2%k ==0):
            return (n*i-(n-1))
        i+=1
    return
n=5
k=4
print("The position of {}\'th multiple of {} in ""Fibonacci Series is {}".format(n,k,findPosition(k, n)))
def fibonacci_num(n):
    fibonacci = [0,1]
    for i in range(0,n):
        if i>=2:
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    return fibonacci
n = int(input("Type the number of terms required: "))
print(fibonacci_num(n))
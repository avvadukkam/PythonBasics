def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
a,b = input("Type the numbers to check : ").split()
print("The largest number is {}".format(maximum(float(a),float(b))))
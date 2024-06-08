def addition(a,b):
    sum = a+b
    print("The sum is ", sum)
a,b = input("Type two numbers to add: ").split()
addition(int(a),int(b))
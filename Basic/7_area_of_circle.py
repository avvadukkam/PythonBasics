def areaCircle(r):
    pi = 3.142
    return pi*r*r
r = int(input("Radius = "))
print("The area of circle with radius {} is {}".format(r,areaCircle(r)))
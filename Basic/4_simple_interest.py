def simple_interest(p,t,r):
    si = p*t*r/100
    return si
p,t,r = input("Type the Principle amount, Term, Rate of Interest : ").split()
print("The simple interest for the amount {}, at a rate of {}% for a term of {} is {}".format(p,r,t,simple_interest(float(p),float(t),float(r))))
def compond_interest(p,t,r):
    a=p*(pow((1+r/100),t))
    return a-p
p,t,r = input("Type the Principle amount, Term, Rate of interest : ").split()
print("The compound interest of the amount {}, over a term of {}, with ROI {}% is {}".format(p,t,r,compond_interest(float(p),float(t),float(r))))
# Using List comprehension
def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [(), ('ram','15','8'),(),('laxman','sita'),('krishna','45'),('','')]
print(Remove(tuples))

# Using filter()
def Remove(tuples1):
    tuples1 = list(filter(None, tuples1))
    return tuples1
tuples1 = [(), ('ram','15','8'),(),('laxman','sita'),('krishna', '45')]
print(Remove(tuples1))
#
def break_list(my_list, n):
    new_list = []
    for i in range(0,len(my_list),n):
        new_list.append(list(my_list[i:i+n]))
    return new_list

my_list = ['geeks', 'for', 'geeks', 'like', 'geeky', 'nerdy',
           'geeks', 'love', 'questions', 'words', 'life']
print(*break_list(my_list, 5))

# Using yield
my_list2 =  ['geeks', 'for', 'geeks', 'like', 'geeky', 'nerdy',
           'geeks', 'love', 'questions', 'words', 'life']
def divide_chunks(l, n):
    for i in range(0, len(l),n):
        yield l[i:i+n]

n = 5
x = list(divide_chunks(my_list2, n))
print(x)

# Using list comprehension
my_list3 = [1,2,3,4,5,6,7,8,9]
n=4
final = [my_list3[i*n:(i+1)*n] for i in range((len(my_list3)+ n -1) //n)]
print(final)

# list comprehension alternate
l = [1,2,3,4,5,6,7,8,9]
n=4
x = [l[i:i+n] for i in range(0,len(l),n)]
print(x)
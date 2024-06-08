# clearing using clear()
A = ["G", 3, 3, "K"]
print("A before clear :", A)
A.clear()
print("A after clearing using clear() : ", A)

# clearing using "*="
B = [1, 2, 3, 4]
print("B before clear : ", B)
B *= 0
print("B after clearing using *= : ", B)

# deleting using reinitialization
C = [5, 6, 7, 8]
print("C before clear : ", C)
C = []
print("C after clearing using reinitialization : ", C)

# deleting using "del"
D = [9, 10, 11, 12]
print("D before clear : ", D)
del D[:]
print("D after clearing using 'del' : ", D)
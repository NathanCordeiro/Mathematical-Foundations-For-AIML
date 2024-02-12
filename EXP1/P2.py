#Program to solve the equation ax + b = cx + d
def equation2(e,f,g,h):
    z=(h-f)/(e-g)
    return z
e = int(input("Enter e:"))
f = int(input("Enter f:"))
g = int(input("Enter g:"))
h = int(input("Enter h:"))
z = equation2(e,f,g,h)
print("x =",z)
equation2(e,f,g,h)
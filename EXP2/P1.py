#Experiment2 Program to solve ax+by=c

def equation(a1,b1,c1,a2,b2,c2):
    print(f"{a1}x + {b1}y = {c1}")
    print(f"{a2}x + {b2}y = {c2}")
    z1 = (c2 * a1) - (a2 * c1)
    z2 = (a1 * b2) - (a2 * b1)
    y = z1 / z2
    return y


a1 = int(input("Enter coefficient a1:"))
b1 = int(input("Enter coefficient b1:"))
c1 = int(input("Enter coefficient c1:"))

a2 = int(input("Enter coefficient a2:"))
b2 = int(input("Enter coefficient b2:"))
c2 = int(input("Enter coefficient c2:"))


y = equation(a1,b1,c1,a2,b2,c2)
print("y = ",y)

x = (c1 - b1 * y) / a1
print("x = ",x)

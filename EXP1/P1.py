#Program to solve the equation ax + b = c
def equation1(a,b,c):
    x=(c-b)/a
    return x

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
x=equation1(a,b,c)
print("x=",x)
equation1(a,b,c)
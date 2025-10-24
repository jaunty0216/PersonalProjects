import math as ma
def calculating(x,y,z):
    distance = ma.sqrt(x**2+y**2+z**2)
    return distance

X = int(input("Enter x:"))
Y = int(input("Enter y:"))
Z = int(input("Enter z:"))
print(calculating(X,Y,Z))
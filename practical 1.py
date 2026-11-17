from math import *
a = float(input("Введите параметр a: "))
z1 = ((1+a+a**2)/(2*a+a**2)+2-(1-a+a**2)/(2*a-a**2))**(-1)*(5-2*a**2)
print("z1 = {0:.4f}".format(z1))
z2 = (4-a**2)/2
print("z2 = {0:.4f}".format(z2))
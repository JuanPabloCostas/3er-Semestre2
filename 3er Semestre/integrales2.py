# Integral con una ecuacion compleja sen(32)^3
import math as m

while done != True:
    

def traductorX(x):
    y = 2*x^3
    return y

limI = int(input("Ingrese el Limite Inferior> "))
limF = int(input("Ingrese el Limite Final> "))
n = 10000
h = (limF-limI)/n




xi= limI
xf= xi + h
yi= traductorX(xi)
yf= traductorX(xf)
Al = (yf+yi)/2*h
for i in range(n-1):
    xi += h
    xf += h
    yi= traductorX(xi)
    yf= traductorX(xf)
    Al += (yf+yi)/2*h

print("Area:",Al)
# Integral con una ecuacion compleja sen(32)^3
import math as m

def traductorX(x):
    y = m.sin(m.radians(9*(x)))**4
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
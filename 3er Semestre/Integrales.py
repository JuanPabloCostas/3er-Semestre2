
def traductorX(x):
    y = (15*(x)**4)**(1/2)
    return y

limI = float(input("Ingresa el limite inferior> "))
limF = float(input("Ingresa el limite superior> "))
n = 1000
h = (limF-limI)/n



Al = 0
xi= limI
xf= xi + h
yi= traductorX(xi)
yf= traductorX(xf)
Al += (yf+yi)/2*h
for i in range(n-1):
    xi += h
    xf += h
    yi= traductorX(xi)
    yf= traductorX(xf)
    Al += (yf+yi)/2*h

print("Area:",Al)

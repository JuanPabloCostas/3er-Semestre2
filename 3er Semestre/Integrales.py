
def traductorX(x):
    y = x**2
    return y

limI = float(input("Ingresa el limite inferior> "))
limF = float(input("Ingresa el limite superior> "))
n = int(input("Ingresa el numero de vueltas> "))
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

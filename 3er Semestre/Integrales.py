# Integral con una ecuacion simple 5(x)^2+2

def traductorX(x):
    y = (328*(x)**25)**(1/9)
    return y

limI = 120
limF = 540
n = 10000
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

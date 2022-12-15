# Integral con una ecuacion simple 5(x)^2+2
import sympy as s

def traductorX(x,ecuacion):
    
    ecuacion = s.sympify(ecuacion.replace("x",str(x)))
    y = float(ecuacion)
    return y

ecuacion = "2*x**2 + 5"
limI = 120
limF = 540
n = 300
h = (limF-limI)/n



Al = 0
xi= limI
xf= xi + h
yi= traductorX(xi,ecuacion)
yf= traductorX(xf,ecuacion)
Al += (yf+yi)/2*h
for i in range(n-1):
    xi += h
    xf += h
    yi= traductorX(xi,ecuacion)
    yf= traductorX(xf,ecuacion)
    Al += (yf+yi)/2*h

print("Area:",Al)

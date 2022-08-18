
#Experimentos
#JuanPaCostas
import random

a = 1
b = -2
c = 3
d = -4
e = -2
f = -9
g = 5
h = -5
i = 7

derivadas = []
derivadas.append(a*8)
derivadas.append(b*7)
derivadas.append(c*6)
derivadas.append(d*5)
derivadas.append(e*4)
derivadas.append(f*3)
derivadas.append(g*2)
derivadas.append(h*1)


for k in range(0,10):
    x = random.randint(0,10000)
    print("X= ",x)
    i = 1
    oldx = None
    while i > 0:
        fx = a*x**8 + b*x**7 + c*x**6 + d*x**5 + e*x**4 + f*x**3 + g*x**2 + h*x**1 + i
        fxd = derivadas[0]*x**7 + derivadas[1]*x**6 + derivadas[2]*x**5 + derivadas[3]*x**4 + derivadas[4]*x**3 + derivadas[5]*x**2 + derivadas[6]*x**1 + derivadas[7]
        x = x - fx/fxd        
        if oldx == x:
            i = 0
        oldx = x
    print("raiz= ",x)
    

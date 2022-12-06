# Integral con una ecuacion compleja sen(32)^3
import math as m
import sympy as s

x = s.symbols('x')

def preguntarEcuacion():
    return s.sympify(input("Ingrese la Ecuacion (2*x^2+3)^2 > "))

def traductorX(x, ecuacionArray):
    for i in range 
        ecuacionArray[1][i]
    y = 2*x^3
    return y

done = False
ecuacionArray = []
while done != True:
    builder = []
    term = int(input("Ingrese si quiere sacar: 1-Seno, 2-Coseno, 3-Tangente, 4-Ecuacion Sola, 5-Termine> "))
    if(term == 5):
        done = True
    elif(term >= 1 and term <= 4):
        if term == 4:
            exponente = 1
        else:
            exponente = int(input("Ingrese el exponente de la funcion trigonometrica> "))
        builder.append(preguntarEcuacion())
        builder.append(term)
        builder.append(exponente)
        ecuacionArray.append(builder)
    else:
        print("Porfavor ingrese un numero del 1 al 5")


print(ecuacionArray)






limI = int(input("Ingrese el Limite Inferior> "))
limF = int(input("Ingrese el Limite Final> "))
n = 10000
h = (limF-limI)/n




xi= limI
xf= xi + h
yi= traductorX(xi, ecuacionArray)
yf= traductorX(xf, ecuacionArray)
Al = (yf+yi)/2*h
for i in range(n-1):
    xi += h
    xf += h
    yi= traductorX(xi, ecuacionArray)
    yf= traductorX(xf, ecuacionArray)
    Al += (yf+yi)/2*h

print("Area:",Al)
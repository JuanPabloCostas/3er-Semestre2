import abc
import os
os.system('cls||clear')

# ex = int(input("Ingresa el exponente> "))
# exGeneral = int(input("Ingrese el exponente> "))
exGeneral = 3
ecuaciones = []

constante = 2
exA = exGeneral
exB = 0
for i in range(0,exA+1):
    if exA == 0 and exB == 0:
        auxC = "1"
    elif constante == 1:
        auxC = ""
    else:
        auxC= str(int(constante))

    if exA == 0:
        auxA = ""
    elif exA == 1:
        auxA = "a"
    else:
        auxA = "a^"+str(exA)

    if exB == 0:
        auxB = ""
    elif exB == 1:
        auxB = "b"
    else:
        auxB = "b^"+str(exB)

    ecuaciones.append(auxC+auxA+auxB)
    constante = constante * exA / (exB+1)
    exA = exA-1
    exB = exB+1
ej = (str(ecuaciones)).replace(","," +").replace("'","").replace("[","").replace("]","").center(140)
print(ej) 
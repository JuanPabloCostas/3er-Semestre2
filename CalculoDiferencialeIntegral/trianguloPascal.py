import abc
import os
os.system('cls||clear')

# ex = int(input("Ingresa el exponente> "))
exGeneral = int(input("Ingrese el exponente> "))

ecuaciones = []

for k in range(0,exGeneral+1):
    ecuaciones.clear()

    constante = 1
    exA = k
    exB = 0
    for i in range(0,k+1):
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

        ecuaciones.append(auxC)
        constante = constante * exA / (exB+1)
        exA = exA-1
        exB = exB+1
    ej = (str(ecuaciones)).replace(",","").center(120)
    print(ej) 
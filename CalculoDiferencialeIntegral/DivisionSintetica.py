import os
import random
os.system('cls||clear')

str = "7x^5+4.3x^4+7.87x^3+7.083x^2+3.3747x+11.03723"
# str = input("Ingrese la ecuacion> ")
alt = str

alt = alt.replace("+", "@")
alt = alt.replace("-", "@-")

constantes = []
constantes.extend(alt.split("@"))

exponentes = []

for i in range (0, len(constantes)):
    consexp = []
    alerta = False
    cons = constantes[i].replace("x", "")
    if constantes[i] == cons:
        alerta = True
    consexp.extend(cons.split("^"))
    if consexp[0] == "":
        constantes[i] = "1"
    else:
        constantes[i] = consexp[0]
    if len(consexp) >= 2:
        exponentes.append(consexp[1])
    else:
        if alerta:
            exponentes.append("0")
        else: 
            exponentes.append("1")
    
inputs = []
for i in range (0,len(constantes)):
    inputs.append(float(constantes[i]))

integers = []
for i in range (0,len(exponentes)):
    integers.append(float(exponentes[i]))

derivadas = []
for i in range (0,(len(integers))):
    derivadas.append(inputs[i]*integers[i])

print("Contantes: ",inputs)
print("Exponentes: ", integers)
print("Derivadas: ",derivadas)

print("")
# posRaiz = float(input("Ingrese la posible raiz> "))
posRaiz = -1.109726227714059
alt = []
resultados = []
resultados.append(inputs[0])
for i in range(0,(len(inputs)-1)):
    alt.append(resultados[i]*posRaiz)
    resultados.append(inputs[i+1]+alt[i])
print(resultados)

if resultados[len(resultados)-1] == 0:
    print(posRaiz, "es una raiz")
else:
    print(posRaiz, "no es una raiz")
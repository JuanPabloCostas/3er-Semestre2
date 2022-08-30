import os
import random
os.system('cls||clear')

str = "10x^5+10x^3-2x+15"
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

p = int(inputs[len(inputs)-1])
q = int(inputs[0])


def sacarComunes(a):
    comunes = []
    for i in range(1,(a+1)):
        if(a%i)==0:
            comunes.append(i)
    return comunes

numeradores = sacarComunes(p)
denominadores = sacarComunes(q)

print("Posibles Raizes:")
for i in range(0,len(denominadores)):
    for k in range(0,len(numeradores)):
        print(numeradores[k],"/",denominadores[i])
    print("")






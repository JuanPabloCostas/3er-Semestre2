import os
os.system('cls||clear')

str = input("Ingrese la ecuacion> ")
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


def cambiosDeSigno(inputs):
    cantcambios = -1
    oldState = -1
    for i in range (0, len(inputs)):
        if inputs[i] > 0:
            currentState = 1
        else:
            currentState = 0
        if currentState != oldState:
            cantcambios = cantcambios +1
        oldState = currentState
    return cantcambios

def cambiosDeSignoNeg(inputs, integers):
    cantcambios = -1
    oldState = -1
    for i in range(0,len(inputs)):
        if integers[i] == 0:
            if inputs[i] > 0:
                currentState = 1
            else:
                currentState = 0
        else:
            if inputs[i]*(-1)**integers[i] > 0:
                currentState = 1
            else:
                currentState = 0
            
        if currentState != oldState:
            cantcambios = cantcambios +1

        oldState = currentState
    return cantcambios

i = cambiosDeSigno(inputs)
pos = cambiosDeSigno(inputs)
neg = cambiosDeSignoNeg(inputs, integers)
img = integers[0]-(pos+neg)
alt = i
listado = []
print("Postivos     Negativos   Imaginarios")
while i >= 0:
    listado.append(pos-(alt-i))
    listado.append(neg)
    listado.append(img+(alt-i))
    print(listado)
    listado.clear()
    i = i - 2





    

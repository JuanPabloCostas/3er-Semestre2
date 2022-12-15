import os
import random
import sympy as s
os.system('cls||clear')



x = s.symbols('x')
part1 = s.sympify("2*x + 5")
part2 = s.sympify("3*x**2 + 2*x")
part2 = -(part2)
final = str(part1)+str(part2)
str = final
# str = input("ingrese> ")
alt = str

alt = alt.replace("+", "@")
alt = alt.replace("-", "@-")
alt = alt.replace("**", "^")
alt = alt.replace("*", "")
alt = alt.replace(" ", "")

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



# float("Constantes: ",constantes)

x = 0
fx = 0
fxd = 0


raices = []

while len(raices) < 2:
    x = random.uniform(-50,50)
    i = 1
    raiz = None
    oldx = x
    fx = 0
    fxd = 0
    while i > 0:
        for i in range (0,len(inputs)):
            if integers[i] == 0:
                fx = fx + inputs[i]
            else:
                fx = fx + inputs[i]*x**integers[i]
        # fx = inputs[0]*x**8 + inputs[1]*x**7 + inputs[2]*x**6 + inputs[3]*x**5 + inputs[4]*x**4 + inputs[5]*x**3 + inputs[6]*x**2 + inputs[7]*x**1 + inputs[8]
        for i in range (0,(len(derivadas))):
            if (integers[i]-1) == 0:
                fxd = fxd + derivadas[i]
            else:
                fxd = fxd + derivadas[i]*x**(integers[i]-1)
                
        # fxd = derivadas[0]*(x**7) + derivadas[1]*(x**6) + derivadas[2]*(x**5) + derivadas[3]*(x**4) + derivadas[4]*(x**3) + derivadas[5]*(x**2) + derivadas[6]*(x**1) + derivadas[7]
        x = x - fx/fxd
        fx = 0
        fxd = 0
        # print("x=",x)
        # print("fx=",fx)
        # print("fxd=",fxd)
        if (oldx - x) < 0.0000001 and (oldx - x) > -0.0000001 :
            i = 0
            raiz = x
        oldx = x
    stop = False
    for k in range(0,len(raices)):
        if (raices[k] - raiz) < 0.001 and (raiz - raices[k]) < 0.001:
            stop = True
            break
    if stop == False:
        raices.append(raiz)
        print("Raiz",len(raices),"= ",raiz)
print("Se acabo")




# positivos = str.replace("+", "@")
# negativos = str.replace("-", "#")


# hola.extend(positivos.split("@"))

# adios.extend(negativos.split("#"))

# cantPos = len(hola)
# cantNeg = len(adios)-1

# if adios[0] == "":
#     print("El primer valor es negativo")
#     hola.pop(0)
#     cantPos = cantPos-1
# adios.pop(0)


# for i in range (0,len(hola)):
#     print(hola[i])

# print("--------------")

# for i in range (0,len(adios)):
#     print(adios[i])


# print("cantidad de postivos: ",cantPos)
# print("cantidad de negativos: ",cantNeg)


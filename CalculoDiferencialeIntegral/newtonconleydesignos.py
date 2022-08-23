import os
os.system('cls||clear')

# Programa para encontrar la raiz de una ecuacion de caulquier nivel y
# utilizando la ey de signos de descarte
#Juan Pablo Costas

# import re

# ecuacion = input("Ingresa la ecuacion> ")

# constantes = []

# constantes.extend(re.split('+|-', ecuacion))

# for i in range(0,len(constantes)):
#     print(constantes[i])

import re

str = "x^1000+3x^3+2x-200"
alt = str

hola = []
adios = []

str = str.replace("+", "@+")
str = str.replace("-", "#-")

alt = alt.replace("+", "@")
alt = alt.replace("-", "@-")

constantes = []
constantes.extend(alt.split("@"))

exponentes = []

for i in range (0, len(constantes)):
    consexp = []
    cons = constantes[i].replace("x", "")
    consexp.extend(cons.split("^"))
    if consexp[0] == "":
        constantes[i] = "1"
    else:
        constantes[i] = consexp[0]
    if len(consexp) >= 2:
        exponentes.append(consexp[1])
    else:
        exponentes.append("1")

print("Constantes: ",constantes)
print("Exponentes: ", exponentes)


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

print("---------------")

soy = "soy"
juan = "juan"
soyjuan = ("9"+juan)
print(soyjuan)


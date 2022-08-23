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

str = "3x^100+5x^2-2x-6"
alt = str

hola = []
adios = []

str = str.replace("+", "@+")
str = str.replace("-", "#-")

alt = alt.replace("+", "@")
alt = alt.replace("-", "@-")

constantes = []
constantes.extend(alt.split("@"))







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


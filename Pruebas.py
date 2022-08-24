#Calculadora de Ecuacion de 8to nivel
#newton rapson
#JuanPaCostas

import random

inputs = []
inputs.append(float(input("Ingresa el valor de a (x8)> ")))
inputs.append(float(input("Ingresa el valor de b (x7)> ")))
inputs.append(float(input("Ingresa el valor de c (x6)> ")))
inputs.append(float(input("Ingresa el valor de d (x5)> ")))
inputs.append(float(input("Ingresa el valor de e (x4)> ")))
inputs.append(float(input("Ingresa el valor de f (x3)> ")))
inputs.append(float(input("Ingresa el valor de g (x2)> ")))
inputs.append(float(input("Ingresa el valor de h (x1)> ")))
inputs.append(float(input("Ingresa el valor de i ()> ")))

derivadas = []
derivadas.append(inputs[0]*8)
derivadas.append(inputs[1]*7)
derivadas.append(inputs[2]*6)
derivadas.append(inputs[3]*5)
derivadas.append(inputs[4]*4)
derivadas.append(inputs[5]*3)
derivadas.append(inputs[6]*2)
derivadas.append(inputs[7]*1)

# 1
# 2
# 3
# 4
# -3
# 7
# -8
# 9
# 1

for p in range(0, len(derivadas)):
    print(derivadas[p])


# x**2 -2x + 1 (x-1)

# x**3 - 3x**2 + 3x - 1 

# for k in range(0,10):
#     x = random.randint(0,10000)
#     print("X= ",x)
#     i = 1
#     oldx = None
#     while i > 0:
#         fx = inputs[0]*x**8 + inputs[1]*x**7 + inputs[2]*x**6 + inputs[3]*x**5 + inputs[4]*x**4 + inputs[5]*x**3 + inputs[6]*x**2 + inputs[7]*x**1 + inputs[8]
#         fxd = derivadas[0]*x**7 + derivadas[1]*x**6 + derivadas[2]*x**5 + derivadas[3]*x**4 + derivadas[4]*x**3 + derivadas[5]*x**2 + derivadas[6]*x**1 + derivadas[7]
#         x = x - fx/fxd
#         if oldx == x:
#             i = 0
#         oldx = x
#     print("raiz= ",x)

x = 0
fx = 0
fxd = 0
fx = inputs[0]*x**8 + inputs[1]*x**7 + inputs[2]*x**6 + inputs[3]*x**5 + inputs[4]*x**4 + inputs[5]*x**3 + inputs[6]*x**2 + inputs[7]*x**1 + inputs[8]
fxd = derivadas[0]*(x**7) + derivadas[1]*(x**6) + derivadas[2]*(x**5) + derivadas[3]*(x**4) + derivadas[4]*(x**3) + derivadas[5]*(x**2) + derivadas[6]*(x**1) + derivadas[7]
x = x - fx/fxd

print(x)
print(fx)
print(fxd)
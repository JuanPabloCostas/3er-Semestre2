#Calculadora de Ecuacion de 4to nivel
#JuanPaCostas

import random

inputs = []
inputs.append(float(input("Ingresa el valor de a> ")))
inputs.append(float(input("Ingresa el valor de b> ")))
inputs.append(float(input("Ingresa el valor de c> ")))
inputs.append(float(input("Ingresa el valor de d> ")))
inputs.append(float(input("Ingresa el valor de e> ")))
inputs.append(float(input("Ingresa el valor de f> ")))
inputs.append(float(input("Ingresa el valor de g> ")))
inputs.append(float(input("Ingresa el valor de h> ")))
inputs.append(float(input("Ingresa el valor de i> ")))

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

raices = []
while len(raices) < 5:
    x = random.randint(0,10)
    i = 1
    raiz = None
    oldx = None
    while i > 0:
        fx = inputs[0]*x**8 + inputs[1]*x**7 + inputs[2]*x**6 + inputs[3]*x**5 + inputs[4]*x**4 + inputs[5]*x**3 + inputs[6]*x**2 + inputs[7]*x**1 + inputs[8]
        fxd = derivadas[0]*(x**7) + derivadas[1]*(x**6) + derivadas[2]*(x**5) + derivadas[3]*(x**4) + derivadas[4]*(x**3) + derivadas[5]*(x**2) + derivadas[6]*(x**1) + derivadas[7]
        x = x - fx/fxd    
        print("fx= ",fx)    
        print("fxd= ",fxd)
        print("x= ",x)        
        if oldx == x:
            i = 0
            raiz = x
        oldx = x
    stop = False
    for k in range(0,len(raices)):
        if raices[k] == raiz:
            stop = True
            break
    if stop == False:
        raices.append(raiz)
        print("Raiz",len(raices),"= ",raiz)
print("Se acabo")
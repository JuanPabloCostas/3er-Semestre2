import os
import random
os.system('cls||clear')

class ecuacion:
    def __init__(self, constante, exponente):
        self.constante = constante
        self.exponente = exponente

def intify(subject):
    if subject == "":
        return 1
    elif subject == "-":
        return -1
    elif "/" in subject:
        aux = []
        aux.extend(subject.split("/"))
        return int(aux[0]) / int(aux[1])
    else:
        return int(subject)

def aObjeto(imput):
    imput = imput.replace("+","@").replace("-","@-")

    lista = []
    lista.extend(imput.split("@"))

    conjunto = []

    for i in range(len(lista)):
        if "x**" in lista[i]:
            aux = lista[i].split("x**")
            ecuacionCreada = ecuacion(intify(aux[0]),intify(aux[1]))
            conjunto.append(ecuacionCreada)

        elif "x" in lista[i]:
            aux = lista[i].split("x")
            ecuacionCreada = ecuacion(intify(aux[0]),1)
            conjunto.append(ecuacionCreada)

        else:
            ecuacionCreada = ecuacion(intify(lista[i]),0)
            conjunto.append(ecuacionCreada)
    
    return conjunto

a = "2x+5"
b = "3x**2+2x"

a = aObjeto(a)
b = aObjeto(b)

for i in range(len(b)):
    b[i].constante = b[i].constante * -1
conjunto = []
conjunto.extend(a+b)

inputs = []
for i in range (0,len(conjunto)):
    inputs.append(float(conjunto[i].constante))

integers = []
for i in range (0,len(conjunto)):
    integers.append(float(conjunto[i].exponente))

derivadas = []
for i in range (0,(len(integers))):
    derivadas.append(inputs[i]*integers[i])





x = 0
fx = 0
fxd = 0


raices = []
alto = False
loops = 0
while len(raices) < 5 and alto == False:
    
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
        
            if (integers[i]-1) == 0:
                fxd = fxd + derivadas[i]
            else:
                fxd = fxd + derivadas[i]*x**(integers[i]-1)
                
        
        x = x - fx/fxd
        fx = 0
        fxd = 0
        if (oldx - x) < 0.0000001 and (oldx - x) > -0.0000001 :
            i = 0
            raiz = x
        oldx = x
    loops += 1
    if loops > 100:
        alto = True
    stop = False
    for k in range(0,len(raices)):
        if (raices[k] - raiz) < 0.001 and (raiz - raices[k]) < 0.001:
            stop = True
            break
    if stop == False:
        raices.append(raiz)
        print("Raiz",len(raices),"= ",raiz)
    
maximo = max(raices)
print(maximo)




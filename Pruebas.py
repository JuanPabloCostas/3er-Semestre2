
#Experimentos
#JuanPaCostas
import random

a = random.uniform(-500, 500)
b = random.uniform(-500, 500)
c = random.uniform(-500, 500)
d = random.uniform(-500, 500)
e = random.uniform(-500, 500)
f = random.uniform(-500, 500)
g = random.uniform(-500, 500)
h = random.uniform(-500, 500)
i = random.uniform(-500, 500)

derivadas = []
derivadas.append(a*8)
derivadas.append(b*7)
derivadas.append(c*6)
derivadas.append(d*5)
derivadas.append(e*4)
derivadas.append(f*3)
derivadas.append(g*2)
derivadas.append(h*1)

raices = []
oldraiz = None
while len(raices) < 5:
    x = random.uniform(-500000, 500000)
    i = 1
    raiz = None
    oldx = None
    while i > 0:
        fx = a*x**8 + b*x**7 + c*x**6 + d*x**5 + e*x**4 + f*x**3 + g*x**2 + h*x**1 + i
        fxd = derivadas[0]*x**7 + derivadas[1]*x**6 + derivadas[2]*x**5 + derivadas[3]*x**4 + derivadas[4]*x**3 + derivadas[5]*x**2 + derivadas[6]*x**1 + derivadas[7]
        x = x - fx/fxd        
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
    oldraiz = raiz
print("Se acabo")
    

    
def Ordenar(vector,pivote):
    for i in range (0, len(vector)):
        if vector[i] > vector[pivote]:
            aux = vector[pivote]
            vector[pivote] = vector[i]
            vector[i] = aux
    return vector


vector = [8,11,3,29,18,10,22,7]
print(vector)
for k in range (0, len(vector)):
    pivote = k
    vector = Ordenar(vector, pivote)
    print(vector)

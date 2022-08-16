#Algoritmo para descibrir cuantos pasos dara un robot
#JuanPabloCostas

def Pasos(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return Pasos(n-1) + Pasos(n-2)

n = 9
print(Pasos(n))
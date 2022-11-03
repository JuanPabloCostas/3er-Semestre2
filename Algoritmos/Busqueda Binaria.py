#Algoritmo de busqueda binaria
#Juan Pablo Costas
#Jesus Alberto
#Javier Valencia
#Juan Carlos
from time import time

def Ordenar(vector):
    for c in range(0,len(vector)):
        pivote=c
        for i in range(c,len(vector)):
            if vector[i] < vector[pivote]:
                aux = vector[i]
                vector[i] = vector[pivote]
                vector[pivote] = aux
    return vector

def BuscaB(lista, k):
    found = False
    middle = int(len(lista)/2)
    if lista[middle] == k:
        print("Lo encontre")
        found = True
        return found
    if lista[middle] > k and len(lista) > 1:
        return BuscaB(lista[:middle],k)
    if lista[middle] < k and len(lista) > 1:
        return BuscaB(lista[middle:],k)
    return found

lista = [15,19,31,10,11,22,71]
k = 11



listaO = Ordenar(lista)
print(listaO)
t0 = time()
a = BuscaB(listaO, k)

t1 = time()
print(a)
print("Tiempo: ", t1-t0)
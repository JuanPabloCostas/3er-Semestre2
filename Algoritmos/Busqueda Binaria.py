#Algoritmo de busqueda binaria
#Juan Pablo Costas
#Jesus Alberto
#Javier Valencia
#Juan Carlos
from time import time

def Ordenar(vector):
    comparaciones = 0
    for c in range(0,len(vector)):
        pivote=c
        for i in range(c,len(vector)):
            comparaciones = comparaciones + 1
            if vector[i] < vector[pivote]:
                aux = vector[i]
                vector[i] = vector[pivote]
                vector[pivote] = aux
    print("Comparaciones= ", comparaciones)
    return vector

def BuscaB(lista, k, lenA):
    lenA = lenA
    middle = int(len(lista)/2)
    if lista[middle] == k:
        location = lenA + middle
        print("Lo encontre en la posicion", location)
        return location
    if lista[middle] > k and len(lista) > 1:
        return BuscaB(lista[:middle],k,lenA)
    if lista[middle] < k and len(lista) > 1:
        lenA = lenA + (len(lista)-len(lista[middle+1:]))
        return BuscaB(lista[middle+1:],k, lenA)
    return False

lista = [63, 94, 111, 125, 204, 209, 250, 290, 310, 348, 420]
k = 290



listaO = Ordenar(lista)
print("Lista ordenada", listaO)
t0 = time()
a = BuscaB(listaO, k, 0, 0)

t1 = time()
print(a)
print("Tiempo: ", t1-t0)
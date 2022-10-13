import numpy as np
from time import time

def mergeSort(alista):
    print("Divide", alista)
    if len(alista)> 1:
        mitad = len(alista)//2
        ladoIzquierdo = alista[:mitad]
        ladoDerecho = alista[mitad:]
        mergeSort(ladoIzquierdo)
        mergeSort(ladoDerecho)
        i = 0
        j = 0
        k = 0
        while i < len(ladoIzquierdo) and j < len(ladoDerecho):
            if ladoIzquierdo[i] < ladoDerecho[j]:
                alista[k] = ladoIzquierdo[i]
                i = i+1
            else:
                alista[k] = ladoDerecho[j]
                j = j+1
            k = k+1
        while i < len(ladoIzquierdo):
            alista[k] = ladoIzquierdo[i]
            i = i+1
            k = k+1
        while j < len(ladoDerecho):
            alista[k] = ladoDerecho[j]
            j = j + 1
            k = k+1
        print("Mezclando", alista)

alista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36,1,100,245,382,920,345,675,129,322,432,396]
print("Lista original", alista)
t0 = time()
mergeSort(alista)
t1 = time()
print("Lista final", alista)
print("Tiempo: {0:f} segundos".format(t1-t0))
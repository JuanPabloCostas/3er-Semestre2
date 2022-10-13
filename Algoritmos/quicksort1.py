
from time import time

def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

miLista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36,1,100,245,382,920,345,675,129,322,432,396]
print("Lista Original", miLista)
t0 = time()
print("Lista Final", sort(miLista))
t1 = time()
print("Tiempo: {0:f} segundos".format(t1-t0))
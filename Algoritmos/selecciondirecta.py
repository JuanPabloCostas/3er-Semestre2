
from time import time

def seleccion(A):
    for i in range(len(A)):
        minimo=i
        for j in range(i,len(A)):
            if(A[j] < A[minimo]):
                minimo=j
        if(minimo != i):
            aux=A[i]
            A[i]=A[minimo]
            A[minimo]=aux
    print("Lista Final", A)
 

A = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36,1,100,245,382,920,345,675,129,322,432,396]
print("Lista Original", A)
t0 = time()
seleccion(A)

t1 = time()
print("Tiempo: {0:f} segundos".format(t1-t0))

from time import time

def insercion(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j]
                A[j]=A[j-1]
                A[j-1]=aux
    print("Lista Final", A)
 

A = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36,1,100,245,382,920,345,675,129,322,432,396]
print("Lista Original", A)
t0 = time()
insercion(A)
t1 = time()
print("Tiempo: {0:f} segundos".format(t1-t0))
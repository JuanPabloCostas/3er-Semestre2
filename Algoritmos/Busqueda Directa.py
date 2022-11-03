#Algoritmo de busqueda directa
#Juan Pablo Costas

def BusquedaD(vector, k):
    found = False
    for i in range(len(vector)):
        if k == vector[i]:
            print("Lo encontre en la posicion: ", i+1)
            found = True
    if found != True:
        print("No lo encontre")
    return


vector = [15,19,31,10,11,22,71]
k = 11

BusquedaD(vector, k)
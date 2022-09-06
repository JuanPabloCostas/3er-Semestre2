# Algoritmo rapido QuickSort
# Costas Rueda Juan Pablo

def Dividir(lista,izq,der):
    pivote = int(len(lista)/2)
    for i in range (len(lista)):
        if lista[i]<pivote:
            izq.append(lista[i])
        else:
            der.append(lista[i])
    if len


        

izq = []
der = []
lista = [9,5,6,4,7,8,3,2,1]
Dividir(lista,izq,der)
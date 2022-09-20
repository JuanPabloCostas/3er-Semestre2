# Algoritmo rapido QuickSort
# Costas Rueda Juan Pablo

def Dividir(lista):
    izq = []
    der = []
    pivote = lista[int(len(lista)/2)]
    print("Pivote= ",pivote)
    for i in range (len(lista)):
        if lista[i]<pivote:
            izq.append(lista[i])
        else:
            der.append(lista[i])
    print(izq)
    print(der)
    if len(izq) > 1:
        Dividir(izq)
    if len(der) > 1:
        Dividir(der)


        


lista = [9,5,6,4,7,8,3,2,1]
Dividir(lista)
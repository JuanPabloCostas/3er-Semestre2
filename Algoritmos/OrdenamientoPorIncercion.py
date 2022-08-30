# Algoritmo para ordenar los valores de una lista de menor a mayor utilizando el metodo de incercion
# Juan Pablo Costas

def Ordenar(lista):
    for i in range (len(lista)-1,-1):
        key = lista[i]
        for k in range(len(lista)-1,-1):
            if(key<=lista[k]):
                lista[k+1]=lista[k]
                posi = k
        lista[posi]=key
    return lista
        

lista = [1,3,2,6,5,9,8,7,4]
print(Ordenar(lista))
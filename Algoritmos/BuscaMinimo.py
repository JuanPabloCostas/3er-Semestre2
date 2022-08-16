#Algoritmo que encuentre el minimo valor de una lista
#JuanPaCostas

def BuscaMinimo(lista):
    menor = lista[0]
    longitud = len(lista)
    for i in range (1, longitud):
        if lista[i] < menor:
            menor = lista[i]
    return menor

lista = [12,33,66,22,7,4,45]
print("La lista es: ", lista)
print ("El menor de la lista es ", BuscaMinimo(lista))

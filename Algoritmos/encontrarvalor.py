#Juego de busqueda binaria
# Juan Pablo
# Maria Jose
# Andrea
# Daniel Ruiz


from random import randint


lista = []
for i in range (1,301):
    lista.append(i)
k = randint(1,300)


def BuscaB(lista, k, lenA):
    print(lista)
    print("")
    lenA = lenA
    middle = int(len(lista)/2)
    if lista[middle] == k:
        location = lenA + middle
        print("Lo encontre es:", location+1)
        return location
    if lista[middle] > k and len(lista) > 1:
        return BuscaB(lista[:middle],k,lenA)
    if lista[middle] < k and len(lista) > 1:
        lenA = lenA + (len(lista)-len(lista[middle+1:]))
        return BuscaB(lista[middle+1:],k, lenA)
    return False

BuscaB(lista,k,0)

print("k= ",k)


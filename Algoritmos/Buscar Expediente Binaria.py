#Algoritmo para encontrar el expediente de un alumno
# Juan Pablo
# Maria Jose
# Andrea
# Daniel Ruiz

def quicksort(lista):
    pivote = lista[0]

    i = 1
    j = len(lista)-1
    
    if len(lista) > 1:
        while i<j:
            while lista[i] < pivote and i < j:
                i += 1
            
            while lista[j] >= pivote and j >= 0:
                j -= 1
            
            if(i < j):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

            a = 1

    if lista[j] <= pivote:
        lista[0] = lista[j]
        lista[j] = pivote

    if len(lista[:j]) > 2:
        lista = quicksort(lista[:j]) + lista[j:]

    if len(lista[j:]) > 2:
        lista = lista[:j+1] + quicksort(lista[j+1:])
    return lista



expedientes = [
[301591, "BARRETO RIVAS GEOVANI"],
[301594, "CARRERA CARRION JOSE CARLOS"],
[301623, "CHAVEZ HERRERA AXEL SEBASTIAN"],
[301568, "FRANCO ESCOBEDO EMILIO"],
[301617, "GARFIAS HERNANDEZ GERMAN EMILIO"],
[301585, "GRANADOS CHAVEZ DANIEL"],
[301634, "JIMENEZ GALEANA OSCAR"],
[301613, "MARTINEZ PEREZ BRYAN JESUS"],
[301565, "MATOS QUEIROZ DE LIMA FABRICIO"],
[301588, "PEREZ VARELA LUIS JAVIER"],
[301572, "QUEIJEIRO ALBO PABLO YAUMA"],
[301577, "RAMIREZ ROJAS DIANA GUADALUPE"],
[301598, "RANGEL ZAMORANO JOSE LUIS"],
[301620, "URIBE DOPHE JIMENA"],
[301606, "WUOTTO FLORES DANIELA"],
[301630, "ZUÑIGA TAPIA RICARDO ARTURO"]
]

def BuscaB(lista, k, lenA):
    lenA = lenA
    middle = int(len(lista)/2)
    if lista[middle][0] == k:
        location = lenA + middle
        print("Lo encontre en la posicion", location)
        return location
    if lista[middle][0] > k and len(lista) > 1:
        return BuscaB(lista[:middle],k,lenA)
    if lista[middle][0] < k and len(lista) > 1:
        lenA = lenA + (len(lista)-len(lista[middle+1:]))
        return BuscaB(lista[middle+1:],k, lenA)
    return False

expedientes = (quicksort(expedientes))
k = 301630
loc = BuscaB(expedientes,k,0)
print(expedientes[loc][1])



# print(BuscarExpediente(expedientes,k))




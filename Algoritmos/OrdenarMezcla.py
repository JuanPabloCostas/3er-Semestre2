# bla balb abalba
#Juan Pablo

def OrdenarMezcla(lista):
    if(len(lista) > 1):
        mitad = len(lista)//2
        izq = lista[:mitad]
        der = lista[mitad:]
        OrdenarMezcla(izq)

    
    return listaE

lista = [8,6,4,2,1,9,7,5,3]
print(OrdenarMezcla(lista))
# Algoritmo para encontrar un vector igual
# Juan Pablo Costas
# Daniel Ruiz Chaparro
# Annd

def Buscar(x, vector):
    foundx = False
    for i in range(len(vector)):
        if x == vector[i]:
            print("Lo Encontre!!!, esta en la posicion ", i+1)
            foundx = True
    if foundx == False:
        print("No encontre tu valor :C")
    return

x = input("Que quieres encontrar?> ")

vector = ["15","mn","x","62","ab","12"]

Buscar(x,vector)
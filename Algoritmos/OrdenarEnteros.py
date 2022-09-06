#Algoritmo para ordenar de menor a mayor numeros en una lista
#Juan Pablo Costas
#Javier Valencia Vázquez
#Juan Carlos Salas Gallegos
#Jesús Alberto Vázquez Rioja
#Grupo 30
from time import time
from numpy import *
def Ordenar(vector):
    for c in range(0,len(vector)):
        pivote=c
        for i in range(c,len(vector)):
            if vector[i] < vector[pivote]:
                aux = vector[i]
                vector[i] = vector[pivote]
                vector[pivote] = aux
        print(vector)
            

vector = [8,11,3,29,18,10,22,7]
print(vector)
Ordenar(vector)
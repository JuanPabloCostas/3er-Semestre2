import numpy as np




lugares = ["El pueblito","Juriquilla","Jurica","UAQ", "CU","Menchaca"]

matriz = np.zeros((6,6))
for i in range(6):
    for j in range(6):
        cadena = "Posicion " + str(i) + " " + str(j) + " > "
        a = int(input(cadena))
        matriz[i,j] = a

print(matriz) 
b = []

for i in range(6):
    auxmenor = 100
    for j in range(6):
        if matriz[i,j] < auxmenor and matriz[i,j] > 0 and auxmenor != b[-1]:
            auxmenor = matriz[i,j]
    print(auxmenor)
    b.append(auxmenor)

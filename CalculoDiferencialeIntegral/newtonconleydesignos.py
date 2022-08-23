# Programa para encontrar la raiz de una ecuacion de caulquier nivel y
# utilizando la ey de signos de descarte
#Juan Pablo Costas

constantes = []
maxConst = float(input("De que nivel sera tu ecuacion"))

for i in range (0,maxConst):
    constantes.append(float(input("Ingresa el valor de a (x",(maxConst-i),")> ")))

derivadas = []
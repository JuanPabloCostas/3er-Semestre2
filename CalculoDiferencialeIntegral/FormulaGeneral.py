import os
os.system('cls||clear')
#Programa para sacar X usando la formula general
#JuanPaCostas

a = input("Ingresa el valor de a> ")

listaA = []
listaA.extend(a.split('/'))
if len(listaA)==1:
    a = float(listaA[0])
elif len(listaA)==2:
    a = float(listaA[0])/float(listaA[1])

b = input("Ingresa el valor de b> ")

listaB = []
listaB.extend(b.split('/'))
if len(listaB)==1:
    b = float(listaB[0])
elif len(listaB)==2:
    b = float(listaB[0])/float(listaB[1])

c = input("Ingresa el valor de c> ")

listaC = []
listaC.extend(c.split('/'))
if len(listaC)==1:
    c = float(listaC[0])
elif len(listaC)==2:
    c = float(listaC[0])/float(listaC[1])

part1 = b*-1
part2 = (b**2)-(4*a*c)
part3 = a*2

if part2 >= 0:
    part2 = part2**(1/2)
    x1 = (part1 + part2)/part3
    x2 = (part1 - part2)/part3

    print("X1 = ", x1)
    print("X2 = ", x2)

else:
    part2 = (part2*-1)**(1/2)
    
    print("X1 = ", (part1/part3), " + ", part2/part3, "i")
    print("X2 = ", (part1/part3), " - ", part2/part3, "i") 

#Experimentos
#JuanPaCostas

a = input("Ingresa el valor de a> ")
listaA = []

listaA.extend(a.split('/'))
if len(listaA)==1:
    a = float(listaA[0])
elif len(listaA)==2:
    a = float(listaA[0])/float(listaA[1])

print(a)
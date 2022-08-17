#Experimentos
#JuanPaCostas

inputs = []

inputs.append(input("Ingresa el valor de a> "))
inputs.append(input("Ingresa el valor de b> "))
inputs.append(input("Ingresa el valor de c> "))

for i in range (0,len(inputs)):
    lista = []
    lista.extend(inputs[i].split('/'))
    if len(lista)==1:
        inputs[i] = float(lista[0])
    elif len(lista)==2:
        inputs[i] = float(lista[0])/float(lista[1])
    lista.clear()

part1 = inputs[1]*-1
part2 = (inputs[1]**2)-(4*inputs[0]*inputs[2])
part3 = inputs[0]*2

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

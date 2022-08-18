#Programa para sacar X de 8 ejercicios usando la formula general
#JuanPaCostas

ListaA = [3,5,10,12/5,11/7,2/6,2/6,2.54]
ListaB = [-2,4,9,-7/5,3,-8,8,-1.3]
ListaC = [6,-20,-3,8,-11,-10,-10,9.4]

for i in range (0, len(ListaA)):
    print("Ejercicio ", (i+1))

    part1 = ListaB[i]*-1
    part2 = (ListaB[i]**2)-(4*ListaA[i]*ListaC[i])
    part3 = ListaA[i]*2

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
    
    print("")
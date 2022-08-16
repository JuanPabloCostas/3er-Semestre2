import os
os.system('cls||clear')
#Programa para sacar X usando la formula general
#JuanPaCostas

a = int(input("Ingresa el valor de a> "))
b = int(input("Ingresa el valor de b> "))
c = int(input("Ingresa el valor de c> "))

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

    

    






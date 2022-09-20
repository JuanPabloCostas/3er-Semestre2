# Proyecto de derivadas - 4 pasos de newton
# Juan Pablo Costas

def strtoarray(ecu):
    ecu = ecu.replace("+", "@")
    ecu = ecu.replace("-", "@-")

    constantes = []
    constantes.extend(ecu.split("@"))

    exponentes = []

    for i in range (0, len(constantes)):
        consexp = []
        alerta = False
        cons = constantes[i].replace("x", "")
        if constantes[i] == cons:
            alerta = True
        consexp.extend(cons.split("^"))
        if consexp[0] == "":
            constantes[i] = "1"
        else:
            constantes[i] = consexp[0]
        if len(consexp) >= 2:
            exponentes.append(consexp[1])
        else:
            if alerta:
                exponentes.append("0")
            else: 
                exponentes.append("1")
    
    cons = []
    for i in range (0,len(constantes)):
        cons.append(float(constantes[i]))

    expo = []
    for i in range (0,len(exponentes)):
        expo.append(float(exponentes[i]))

    return cons, expo

def ecuacion4to(binomio):
    constantes = binomio[0]
    exponentes = binomio[1]

    binomios = []
    for i in range(len(constantes)):
        constante = constantes[i]
        exX = exponentes[i]
        exY = 0

        
        for k in range(int(exX+1)):
            ecuacion = []
            
            ecuacion.append(constante)
            ecuacion.append(exX)
            ecuacion.append(exY)

            binomios.append(ecuacion)

            constante = constante*exX/(exY+1)
            exX = exX-1
            exY = exY+1

    print(binomios)
        
    return

ecuacion4to(strtoarray("8x^2-3x"))




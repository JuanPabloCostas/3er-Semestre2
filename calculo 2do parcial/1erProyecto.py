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
    # Paso 1 y 2, se agregan ecuaciones a la lista
    binomios = []
    binomiosNeg = []
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
            if k == 0:
                binomiosNeg.append(ecuacion)

            constante = constante*exX/(exY+1)
            exX = exX-1
            exY = exY+1
    
    # Paso 2, restar binomios
    for i in range(len(binomiosNeg)):
        binomios.remove(binomiosNeg[i])

    # Paso 3, divido h
    for i in range(len(binomios)):
        binomios[i][2] = binomios[i][2] - 1

    # Paso 4, h = 0
    i = 0
    while i < len(binomios):
        if binomios[i][2] != 0:
            binomios.pop(i)
            i = i - 1
        i = i + 1


    # Formato
    formato = []
    for i in range(len(binomios)):
        a = binomios[i][0]
        b = binomios[i][1]
        formato.append(str(int(a))+"x^"+str(int(b)))
        
    print(formato)
    return

ecuacion4to(strtoarray("7x^3-6x+1"))




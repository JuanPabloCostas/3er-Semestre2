from cgitb import text
from tkinter import *
from PIL import ImageTk,Image
import sympy as s
import random
import datetime as date
import numpy as np
import sys


root = Tk()
root.title('Proyecto Final Calculo')


#--------------------------
#MENU
#--------------------------
f_menu = LabelFrame(root,padx=20,pady=20)
f_menu.grid(row=0,column=0,padx=50, pady=10)



f_formula = LabelFrame(root, text="Formula General", padx=10, pady=10)
def s_formula():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_formula.grid(row=0,column=1,padx=10,pady=10)
    l_res = Label(f_formula, text="Ingrese A, B, y C")
    l_res.pack()
    a = Entry(f_formula, width=15)
    b = Entry(f_formula, width=15)
    c = Entry(f_formula, width=15)
    a.pack()
    b.pack()
    c.pack()

    def calular_formula(a,b,c):
        inputs = []

        inputs.append(a)
        inputs.append(b)
        inputs.append(c)

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

            l_x1 = Label(f_formula, text="X1 = " + str(x1))
            l_x1.pack()    
            l_x2 = Label(f_formula, text="X2 = " + str(x2))
            l_x2.pack()  
            # print("X1 = ", x1)
            # print("X2 = ", x2)

        else:
            part2 = (part2*-1)**(1/2)

            l_x1 = Label(f_formula, text="X1 = " + str(part1/part3) + " + " + str(part2/part3) + "i")
            l_x1.pack()    
            l_x2 = Label(f_formula, text="X1 = " + str(part1/part3) + " - " + str(part2/part3) + "i")
            l_x2.pack() 
            # print("X1 = ", (part1/part3), " + ", part2/part3, "i")
            # print("X2 = ", (part1/part3), " - ", part2/part3, "i") 



    b_calcular = Button(f_formula, text="Calcular", command=lambda: calular_formula(a.get(),b.get(),c.get()))
    b_calcular.pack()

f_newton = LabelFrame(root, text="Newton Rapthson", padx=10, pady=10)
def s_newton():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_newton.grid(row=0,column=1,padx=10,pady=10)
    l_res = Label(f_newton, text="Ingresa la ecuacion (2x^2-x+1)")
    l_res.pack()
    alt = Entry(f_newton, width=35)
    alt.pack()

    def cal_newton(alt):

        alt = alt.replace("+", "@")
        alt = alt.replace("-", "@-")

        constantes = []
        constantes.extend(alt.split("@"))

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
            
        inputs = []
        for i in range (0,len(constantes)):
            inputs.append(float(constantes[i]))

        integers = []
        for i in range (0,len(exponentes)):
            integers.append(float(exponentes[i]))

        derivadas = []
        for i in range (0,(len(integers))):
            derivadas.append(inputs[i]*integers[i])

        x = 0
        fx = 0
        fxd = 0


        raices = []

        while len(raices) < 3:
            x = random.uniform(-50,50)
            i = 1
            raiz = None
            oldx = x
            fx = 0
            fxd = 0
            while i > 0:
                for i in range (0,len(inputs)):
                    if integers[i] == 0:
                        fx = fx + inputs[i]
                    else:
                        fx = fx + inputs[i]*x**integers[i]
                # fx = inputs[0]*x**8 + inputs[1]*x**7 + inputs[2]*x**6 + inputs[3]*x**5 + inputs[4]*x**4 + inputs[5]*x**3 + inputs[6]*x**2 + inputs[7]*x**1 + inputs[8]
                for i in range (0,(len(derivadas))):
                    if (integers[i]-1) == 0:
                        fxd = fxd + derivadas[i]
                    else:
                        fxd = fxd + derivadas[i]*x**(integers[i]-1)
                        
                # fxd = derivadas[0]*(x**7) + derivadas[1]*(x**6) + derivadas[2]*(x**5) + derivadas[3]*(x**4) + derivadas[4]*(x**3) + derivadas[5]*(x**2) + derivadas[6]*(x**1) + derivadas[7]
                x = x - fx/fxd
                fx = 0
                fxd = 0
                if (oldx - x) < 0.0000001 and (oldx - x) > -0.0000001 :
                    i = 0
                    raiz = x
                oldx = x
            stop = False
            for k in range(0,len(raices)):
                if (raices[k] - raiz) < 0.001 and (raiz - raices[k]) < 0.001:
                    stop = True
                    break
            if stop == False:
                raices.append(raiz)
                l_raiz = Label(f_newton, text=("Raiz" , len(raices) , "= " , raiz))
                l_raiz.pack()
    
    b_cal_newton = Button(f_newton, text="Calcular", command=lambda: cal_newton(alt.get()))
    b_cal_newton.pack()

f_signos = LabelFrame(root, text="Ley de Signos", padx=10,pady=10)
def s_signos():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_signos.grid(row=0,column=1,padx=10,pady=10)

    l_res = Label(f_signos, text="Ingresa la ecuacion (2x^2-x+1)")
    l_res.pack()

    alt = Entry(f_signos, width=35)
    alt.pack()

    def cal_signos(alt):
        alt = alt.replace("+", "@")
        alt = alt.replace("-", "@-")

        constantes = []
        constantes.extend(alt.split("@"))

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
            
        inputs = []
        for i in range (0,len(constantes)):
            inputs.append(float(constantes[i]))

        integers = []
        for i in range (0,len(exponentes)):
            integers.append(float(exponentes[i]))

        derivadas = []
        for i in range (0,(len(integers))):
            derivadas.append(inputs[i]*integers[i])


        def cambiosDeSigno(inputs):
            cantcambios = -1
            oldState = -1
            for i in range (0, len(inputs)):
                if inputs[i] > 0:
                    currentState = 1
                else:
                    currentState = 0
                if currentState != oldState:
                    cantcambios = cantcambios +1
                oldState = currentState
            return cantcambios

        def cambiosDeSignoNeg(inputs, integers):
            cantcambios = -1
            oldState = -1
            for i in range(0,len(inputs)):
                if integers[i] == 0:
                    if inputs[i] > 0:
                        currentState = 1
                    else:
                        currentState = 0
                else:
                    if inputs[i]*(-1)**integers[i] > 0:
                        currentState = 1
                    else:
                        currentState = 0
                    
                if currentState != oldState:
                    cantcambios = cantcambios +1

                oldState = currentState
            return cantcambios

        # i = cambiosDeSigno(inputs)
        pos = cambiosDeSigno(inputs)
        neg = cambiosDeSignoNeg(inputs, integers)
        i = pos
        k = neg
        img = integers[0]
        listado = []
        while i >= 0:
            listado.append(i)
            listado.append(k)
            listado.append(img-(i+k))
            # print(listado)
            l_list = Label(f_signos, text=str(listado))
            l_list.pack()
            listado.clear()
            if(i == 0 or i == 1):
                break
            else:
                i = i - 2

        while k >= 0:
            if(k == 0 or k == 1):
                break
            else:
                k = k - 2
            listado.append(i)
            listado.append(k)
            listado.append(img-(i+k))
            l_list = Label(f_signos, text=str(listado))
            l_list.pack()
            listado.clear()



    b_signos = Button(f_signos, text="Calcular", command=lambda: cal_signos(alt.get()))
    b_signos.pack()

f_posibles = LabelFrame(root, text="Posibles Raices",padx=10,pady=10)
def s_posibes():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_posibles.grid(row=0,column=1,padx=10,pady=10)

    l_res = Label(f_posibles, text="Ingresa la ecuacion (2x^2-x+1)")
    l_res.pack()
    alt = Entry(f_posibles, width=35)
    alt.pack()

    def cal_posibles(alt):
        alt = alt.replace("+", "@")
        alt = alt.replace("-", "@-")

        constantes = []
        constantes.extend(alt.split("@"))

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
            
        inputs = []
        for i in range (0,len(constantes)):
            inputs.append(float(constantes[i]))

        integers = []
        for i in range (0,len(exponentes)):
            integers.append(float(exponentes[i]))

        derivadas = []
        for i in range (0,(len(integers))):
            derivadas.append(inputs[i]*integers[i])

        p = int(inputs[len(inputs)-1])
        q = int(inputs[0])


        def sacarComunes(a):
            comunes = []
            for i in range(1,(a+1)):
                if(a%i)==0:
                    comunes.append(i)
            return comunes

        numeradores = sacarComunes(p)
        denominadores = sacarComunes(q)

        
        for i in range(0,len(denominadores)):
            for k in range(0,len(numeradores)):
                l_raices = Label(f_posibles, text=str(numeradores[k]) + "/" + str(denominadores[i]))
                l_raices.pack()
                # print(numeradores[k],"/",denominadores[i])
            l_space = Label(f_posibles, text="")
            l_space.pack()

    b_calcular = Button(f_posibles,text="Calcular", command=lambda: cal_posibles(alt.get()))
    b_calcular.pack()

f_sintetica = LabelFrame(root, text="Division Sintetica",padx=10,pady=10)
def s_sintetica():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_sintetica.grid(row=0,column=1,padx=10,pady=10)
    l_res = Label(f_sintetica, text="Ingresa la ecuacion (2x^2-x+1)")
    l_res.pack()
    alt = Entry(f_sintetica, width=35)
    alt.pack()

    l_res = Label(f_sintetica, text="Ingresa el exponente en Entero")
    l_res.pack()
    pos = Entry(f_sintetica, width=35)
    pos.pack()

    def cal_sintetica(alt,pos):
        alt = alt.replace("+", "@")
        alt = alt.replace("-", "@-")

        constantes = []
        constantes.extend(alt.split("@"))

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
            
        inputs = []
        for i in range (0,len(constantes)):
            inputs.append(float(constantes[i]))

        integers = []
        for i in range (0,len(exponentes)):
            integers.append(float(exponentes[i]))

        derivadas = []
        for i in range (0,(len(integers))):
            derivadas.append(inputs[i]*integers[i])

        print("")
        # posRaiz = float(input("Ingrese la posible raiz> "))
        # posRaiz = -1.109726227714059
        pos = float(pos)
        alt = []
        resultados = []
        resultados.append(inputs[0])
        for i in range(0,(len(inputs)-1)):
            alt.append(resultados[i]*pos)
            resultados.append(inputs[i+1]+alt[i])
        print(resultados)

        if resultados[len(resultados)-1] == 0:
            es = " es una raiz"
        else:
            es = " no es una raiz"
        
        l_res = Label(f_sintetica, text=str(pos) + es)
        l_res.pack()

    b_calcular = Button(f_sintetica, text="Calcular", command=lambda: cal_sintetica(alt.get(),pos.get()))
    b_calcular.pack()

f_binomios = LabelFrame(root, text="Binomios de Newton", padx=10,pady=10)
def s_binomios():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_binomios.grid(row=0, column=1, padx=10,pady=10)
    l_res = Label(f_binomios, text="Ingresa el exponente en Entero")
    l_res.pack()
    exGeneral = Entry(f_binomios,width=10)
    exGeneral.pack()

    def cal_binomios(exGeneral):
        ecuaciones = []

        for k in range(exGeneral,exGeneral+1):
            ecuaciones.clear()

            constante = 1
            exA = k
            exB = 0
            for i in range(0,k+1):
                if exA == 0 and exB == 0:
                    auxC = "1"
                elif constante == 1:
                    auxC = ""
                else:
                    auxC= str(int(constante))

                if exA == 0:
                    auxA = ""
                elif exA == 1:
                    auxA = "a"
                else:
                    auxA = "a^"+str(exA)

                if exB == 0:
                    auxB = ""
                elif exB == 1:
                    auxB = "b"
                else:
                    auxB = "b^"+str(exB)

                ecuaciones.append(auxC+auxA+auxB)
                constante = constante * exA / (exB+1)
                exA = exA-1
                exB = exB+1
            ej = (str(ecuaciones)).replace(","," +").replace("'","").replace("[","").replace("]","")
            l_res = Label(f_binomios, text=ej)
            l_res.pack()
            
            # print(ej) 

    b_calcular = Button(f_binomios, text="Calcular", command=lambda: cal_binomios(int(exGeneral.get())))
    b_calcular.pack()

f_pascal = LabelFrame(root, text="Triangulo de Pascal", padx=10,pady=10)
def s_pascal():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_pascal.grid(row=0,column=1,padx=10,pady=10)
    l_res = Label(f_pascal, text="Ingresa el exponente en Entero")
    l_res.pack()
    exGeneral = Entry(f_pascal,width=10)
    exGeneral.pack()

    def cal_pascal(exGeneral):
        ecuaciones = []

        for k in range(0,exGeneral+1):
            ecuaciones.clear()

            constante = 1
            exA = k
            exB = 0
            for i in range(0,k+1):
                auxC= str(int(constante))

                if exA == 0:
                    auxA = ""
                elif exA == 1:
                    auxA = "a"
                else:
                    auxA = "a^"+str(exA)

                if exB == 0:
                    auxB = ""
                elif exB == 1:
                    auxB = "b"
                else:
                    auxB = "b^"+str(exB)

                ecuaciones.append(auxC)
                constante = constante * exA / (exB+1)
                exA = exA-1
                exB = exB+1
            ej = (str(ecuaciones)).replace(",","")
            l_res = Label(f_pascal, text=ej)
            l_res.pack()
            # print(ej)        

    b_calcular = Button(f_pascal, text="Calcular", command=lambda: cal_pascal(int(exGeneral.get())))
    b_calcular.pack()

f_derivadas = LabelFrame(root, text="Derivadas", padx=10,pady=10)
def s_derivadas():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_derivadas.grid(row=0,column=1,padx=10,pady=10)
    l_res = Label(f_derivadas, text="Ingresa la ecuacion (2x^2-x+1)")
    l_res.pack()

    ecu = Entry(f_derivadas,width=10)
    ecu.pack()

    def cal_derivadas(ecu):
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
                if binomios[i][0] == 1:
                    a = ""
                elif binomios[i][0] > 0:
                    a = "+"+str(int(binomios[i][0]))
                else:
                    a = str(int(binomios[i][0]))

                if binomios[i][1] == 0:
                    b = ""
                elif binomios[i][1] == 1:
                    b = "x"
                else:
                    b = "x^"+str(int(binomios[i][1]))

                formato.append(a+b)
                
            yo = str(formato).replace(" ","").replace("[","").replace("]","").replace("'","").replace(","," ")
            l_res = Label(f_derivadas, text=yo)
            l_res.pack()
        
        ecuacion4to(strtoarray(ecu))

    b_calcular = Button(f_derivadas, text="Calcular", command=lambda: cal_derivadas(ecu.get()))
    b_calcular.pack()

f_limites = LabelFrame(root, text="Limites", padx=10, pady=10)
def s_limites():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()

    f_limites.grid(row=0,column=1,padx=10,pady=10)
    l_res = Label(f_limites,text="Ingresa la ecuacion 1 (2*x**2 +5)> ")
    l_res.pack()
    ecu = Entry(f_limites,width=15)
    ecu.pack()
    l_res2 = Label(f_limites,text="Ingresa la ecuacion 2 (2*x**2 +5)> ")
    l_res2.pack()
    ecu1 = Entry(f_limites,width=15)
    ecu1.pack()

    def cal_limites(ecu,ecu1):
        l_res = Label(f_limites, text="Limite de "+ ecu +" y "+ecu1)
        l_res.pack()
        x = s.symbols('x')
        part1 = s.sympify(ecu)
        part2 = s.sympify(ecu1)
        part2 = -(part2)
        final = str(part1)+str(part2)
        alt = final
        # str = input("ingrese> ")
        

        alt = alt.replace("+", "@")
        alt = alt.replace("-", "@-")
        alt = alt.replace("**", "^")
        alt = alt.replace("*", "")
        alt = alt.replace(" ", "")

        constantes = []
        constantes.extend(alt.split("@"))

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
            
        inputs = []
        for i in range (0,len(constantes)):
            inputs.append(float(constantes[i]))

        integers = []
        for i in range (0,len(exponentes)):
            integers.append(float(exponentes[i]))

        derivadas = []
        for i in range (0,(len(integers))):
            derivadas.append(inputs[i]*integers[i])



        # float("Constantes: ",constantes)

        x = 0
        fx = 0
        fxd = 0


        raices = []

        while len(raices) < 2:
            x = random.uniform(-50,50)
            i = 1
            raiz = None
            oldx = x
            fx = 0
            fxd = 0
            while i > 0:
                for i in range (0,len(inputs)):
                    if integers[i] == 0:
                        fx = fx + inputs[i]
                    else:
                        fx = fx + inputs[i]*x**integers[i]
                # fx = inputs[0]*x**8 + inputs[1]*x**7 + inputs[2]*x**6 + inputs[3]*x**5 + inputs[4]*x**4 + inputs[5]*x**3 + inputs[6]*x**2 + inputs[7]*x**1 + inputs[8]
                for i in range (0,(len(derivadas))):
                    if (integers[i]-1) == 0:
                        fxd = fxd + derivadas[i]
                    else:
                        fxd = fxd + derivadas[i]*x**(integers[i]-1)
                        
                # fxd = derivadas[0]*(x**7) + derivadas[1]*(x**6) + derivadas[2]*(x**5) + derivadas[3]*(x**4) + derivadas[4]*(x**3) + derivadas[5]*(x**2) + derivadas[6]*(x**1) + derivadas[7]
                x = x - fx/fxd
                fx = 0
                fxd = 0
                # print("x=",x)
                # print("fx=",fx)
                # print("fxd=",fxd)
                if (oldx - x) < 0.0000001 and (oldx - x) > -0.0000001 :
                    i = 0
                    raiz = x
                oldx = x
            stop = False
            for k in range(0,len(raices)):
                if (raices[k] - raiz) < 0.001 and (raiz - raices[k]) < 0.001:
                    stop = True
                    break
            if stop == False:
                raices.append(raiz)
                l_res = Label(f_limites, text=str(raiz))
                l_res.pack()
    
    b_calcular = Button(f_limites, text="Calcular", command=lambda: cal_limites(ecu.get(),ecu1.get()))
    b_calcular.pack()

f_areas = LabelFrame(root, text="Areas", padx=10,pady=10)
def s_areas():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()
    

    f_areas.grid(row=0,column=1,padx=10,pady=10)
    l_res = Label(f_areas,text="Ingresa la ecuacion (2*x**2 +5)> ")
    l_res.pack()
    ecu = Entry(f_areas,width=15)
    ecu.pack()
    l_res2 = Label(f_areas,text="Ingresa el limite inferior (1)> ")
    l_res2.pack()
    limi = Entry(f_areas,width=15)
    limi.pack()
    l_res3 = Label(f_areas,text="Ingresa el limite superior (2)> ")
    l_res3.pack()
    lims = Entry(f_areas,width=15)
    lims.pack()
    
    def cal_area(ecu,limi,lims):
        l_res = Label(f_areas, text=ecu+" | "+"LI"+" | "+"LS"+" | "+"Area")
        l_res.pack()
        def traductorX(x,ecuacion):
    
            ecuacion = s.sympify(ecuacion.replace("x",str(x)))
            y = float(ecuacion)
            return y

        ecuacion = ecu
        limI = float(limi)
        limF = float(lims)
        n = 300
        h = (limF-limI)/n



        Al = 0
        xi= limI
        xf= xi + h
        yi= traductorX(xi,ecuacion)
        yf= traductorX(xf,ecuacion)
        Al += (yf+yi)/2*h
        for i in range(n-1):
            xi += h
            xf += h
            yi= traductorX(xi,ecuacion)
            yf= traductorX(xf,ecuacion)
            Al += (yf+yi)/2*h

        l_res = Label(f_areas, text=ecu+" | "+str(limI)+" | "+str(limF)+" | "+str(Al))
        l_res.pack()
    
    b_calcular = Button(f_areas, text="Calcular", command=lambda: cal_area(ecu.get(),limi.get(),lims.get()))
    b_calcular.pack()

f_balance = LabelFrame(root, text="Balance", padx=10,pady=10)
def s_balance():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()
    

    f_balance.grid(row=0,column=1,padx=10,pady=10)

    l_ecu1 = Label(f_balance,text="Ingresa la primera ecuacion (2x**2+5)> ")
    l_ecu1.pack()

    ecu1 = Entry(f_balance,width=15)
    ecu1.pack()

    l_ecu2 = Label(f_balance,text="Ingresa la segunda ecuacion (2x**2+5)> ")
    l_ecu2.pack()

    ecu2 = Entry(f_balance,width=15)
    ecu2.pack()

    def cal_balance(ecu1,ecu2):
        class ecuacion:
            def __init__(self, constante, exponente):
                self.constante = constante
                self.exponente = exponente

        def intify(subject):
            if subject == "":
                return 1
            elif subject == "-":
                return -1
            elif "/" in subject:
                aux = []
                aux.extend(subject.split("/"))
                return float(aux[0]) / float(aux[1])
            else:
                return float(subject)

        def integrar(conjunto):
            for i in range(len(conjunto)):
                conjunto[i].exponente += 1
                conjunto[i].constante = conjunto[i].constante / conjunto[i].exponente
            return conjunto

        def sumar(conjunto,superior,inferior):
            aux1 = 0
            for i in range(len(conjunto)):
                aux1 = aux1 + resolver(conjunto[i],superior)
            aux2 = 0
            for i in range(len(conjunto)):
                aux2 = aux2 + resolver(conjunto[i],inferior)
            return aux1 - aux2

        def resolver(ecuacion,x):
            return ecuacion.constante * x ** ecuacion.exponente

        def aObjeto(imput):
            imput = imput.replace(" ","").replace("+","@").replace("-","@-")

            lista = []
            lista.extend(imput.split("@"))

            conjunto = []

            for i in range(len(lista)):
                if "x**" in lista[i]:
                    aux = lista[i].split("x**")
                    ecuacionCreada = ecuacion(intify(aux[0]),intify(aux[1]))
                    conjunto.append(ecuacionCreada)

                elif "x" in lista[i]:
                    aux = lista[i].split("x")
                    ecuacionCreada = ecuacion(intify(aux[0]),1)
                    conjunto.append(ecuacionCreada)

                else:
                    ecuacionCreada = ecuacion(intify(lista[i]),0)
                    conjunto.append(ecuacionCreada)
            
            return conjunto

        def igualar(conjuntoA,conjuntoB):
            auxA = []
            auxB = []
            for i in range(len(conjuntoA)):
                auxA.append(ecuacion(conjuntoA[i].constante,conjuntoA[i].exponente))
            for i in range(len(conjuntoB)):
                auxB.append(ecuacion(conjuntoB[i].constante,conjuntoB[i].exponente))
            for i in range(len(auxB)):
                auxB[i].constante = auxB[i].constante * -1
            conjuntoIgualado = []
            conjuntoIgualado.extend(auxA+auxB)
            return conjuntoIgualado

        def sacarRaiz(conjunto):

            inputs = []
            for i in range (0,len(conjunto)):
                inputs.append(float(conjunto[i].constante))

            integers = []
            for i in range (0,len(conjunto)):
                integers.append(float(conjunto[i].exponente))

            derivadas = []
            for i in range (0,(len(integers))):
                derivadas.append(inputs[i]*integers[i])

            x = 0
            fx = 0
            fxd = 0

            raices = []
            alto = False
            loops = 0
            while len(raices) < 5 and alto == False:
                
                x = random.uniform(-50,50)
                i = 1
                raiz = None
                oldx = x
                fx = 0
                fxd = 0
                while i > 0:
                    for i in range (0,len(inputs)):
                        if integers[i] == 0:
                            fx = fx + inputs[i]
                        else:
                            fx = fx + inputs[i]*x**integers[i]
                    
                        if (integers[i]-1) == 0:
                            fxd = fxd + derivadas[i]
                        else:
                            fxd = fxd + derivadas[i]*x**(integers[i]-1)
                    x = x - fx/fxd
                    fx = 0
                    fxd = 0
                    if (oldx - x) < 0.0000001 and (oldx - x) > -0.0000001 :
                        i = 0
                        raiz = x
                    oldx = x
                loops += 1
                if loops > 1000:
                    alto = True
                stop = False
                for k in range(0,len(raices)):
                    if (raices[k] - raiz) < 0.001 and (raiz - raices[k]) < 0.001:
                        stop = True
                        break
                if stop == False:
                    raices.append(raiz)
                
            return max(raices)


        a = ecu1
        b = ecu2

        a = aObjeto(a)
        b = aObjeto(b)


        superior = sacarRaiz(igualar(a,b))
        inferior = 0



        a = integrar(a)
        b = integrar(b)



        resultado = []


        resultado.append(sumar(a,superior,inferior))
        resultado.append(sumar(b,superior,inferior))

        resultado = max(resultado)-min(resultado)
        print("Punto de equilibrio", superior)

        print("Monto de retornar", resultado)

        print("Punto de retorno", sacarRaiz(igualar(a,b)))

        
        l_res = Label(f_balance, text="Punto de equilibrio: " + str(round(superior,4)))
        l_res.pack()

        l_res = Label(f_balance, text="Monto de retorno: " + str(round(resultado,4)))
        l_res.pack()

        l_res = Label(f_balance, text="Punto de retorno: " + str(round(sacarRaiz(igualar(a,b)),4)))
        l_res.pack()

        
    
    b_calcular = Button(f_balance, text="Calcular", command=lambda: cal_balance(ecu1.get(),ecu2.get()))
    b_calcular.pack()

f_rectas = LabelFrame(root, text="Rectas", padx=10,pady=10)
def s_rectas():
    f_formula.grid_forget()
    f_newton.grid_forget()
    f_signos.grid_forget()
    f_posibles.grid_forget()
    f_sintetica.grid_forget()
    f_binomios.grid_forget()
    f_pascal.grid_forget()
    f_derivadas.grid_forget()
    f_limites.grid_forget()
    f_areas.grid_forget()
    f_autor.grid_forget()
    f_autor1.grid_forget()
    

    f_rectas.grid(row=0,column=1,padx=10,pady=10)
    l_mes = Label(f_rectas,text="Ingrese el mes en digitos (1-12)> ")
    l_mes.pack()

    mes = Entry(f_rectas,width=15)
    mes.pack()

    l_dia = Label(f_rectas,text="Ingrese el dia en digitos (1-31)> ")
    l_dia.pack()

    dia = Entry(f_rectas,width=15)
    dia.pack()

    l_valor = Label(f_rectas,text="Ingrese el valor> ")
    l_valor.pack()

    valor = Entry(f_rectas,width=15)
    valor.pack()


    def calcular_recta(registros):
        def isPos(valor):
            if valor >= 0:
                return "+"
            else:
                return ""

        n = len(registros)

        x = 0

        yacumTemporal = 0
        yacum = 0

        xy = 0

        x2y = 0

        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        for i in range(n):
            x += registros[i].x

            yacumTemporal += registros[i].y
            yacum += yacumTemporal

            xy += registros[i].x * yacumTemporal

            x2y += registros[i].x ** 2 * yacumTemporal

            x2 += registros[i].x ** 2
            x3 += registros[i].x ** 3
            x4 += registros[i].x ** 4



        # Reading number of unknowns
        nt = 3

        # Making numpy array of n x n+1 size and initializing 
        # to zero for storing augmented matrix
        a = np.zeros((nt,nt+1))
        # Making numpy array of n size and initializing 
        # to zero for storing solution vector
        xt = np.zeros(nt)
        # Reading augmented matrix coefficients
        a[0][0] = n
        a[0][1] = x
        a[0][2] = x2
        a[0][3] = yacum
        a[1][0] = x
        a[1][1] = x2
        a[1][2] = x3
        a[1][3] = xy
        a[2][0] = x2
        a[2][1] = x3
        a[2][2] = x4
        a[2][3] = x2y

        # Applying Gauss Jordan Elimination
        for i in range(nt):
            if a[i][i] == 0.0:
                print(i)
                sys.exit('Divide by zero detected!')
                
            for j in range(nt):
                if i != j:
                    ratio = a[j][i]/a[i][i]

                    for k in range(nt+1):
                        a[j][k] = a[j][k] - ratio * a[i][k]

        # Obtaining Solution

        for i in range(nt):
            xt[i] = a[i][nt]/a[i][i]

        l_res = Label(f_rectas, text="Ecuacion")
        l_res.pack()

        l_res = Label(f_rectas, text=str(round(xt[2],3))+"x**2"+isPos(xt[1])+str(round(xt[1],3))+"x"+isPos(xt[1])+str(round(xt[0],3)))
        l_res.pack()

        
        
    
    class registro:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def addRegistro(month, day, y):
        x = int(date.date(int(date.date.today().strftime("%Y")),month,day).strftime("%j"))
        return registro(x, y)
    
    registros = []
    b_anandir = Button(f_rectas, text="Añadir", command=lambda: registros.append(addRegistro(int(mes.get()),int(dia.get()),float(valor.get()))))
    b_anandir.pack()

    b_calcular = Button(f_rectas, text="Calcular", command=lambda: calcular_recta(registros))
    b_calcular.pack()

f_autor = LabelFrame(root, text="Autor = Costas Rueda Juan Pablo",padx=10,pady=10)
f_autor1 = LabelFrame(root,text="Autor",padx=10,pady=10)
def s_autor():
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

    f_autor.grid(row=0,column=1, padx=10,pady=10)
    

    my_img = ImageTk.PhotoImage(Image.open("juan1.png"))
    l_img = Label(f_autor,image=my_img)
    
    
    
    

    cadena = """Costas Rueda Juan Pablo
    jcostas29@alumnos.uaq.mx
    307081

    Me llamo Juan Pablo Costas,
    estoy estudiando para convertirme en ingeniero 
    de software, me la paso desvelandome.

    En el poco tiempo libre que tengo suelo ver anime
    y jugar videojuegos.

    Me gustan mucho los perros y los gatos.
    """
    f_autor1.grid(row=2,column=1, padx=10,pady=10)
    l_text = Label(f_autor1, text=cadena)
    l_text.pack()

    l_text = Label(f_autor, text=cadena)

    # l_text.pack()
    l_img.grid(row=0,column=0)
    l_text.pack(row=1,column=0)
    

    





b_formula = Button(f_menu, text="Formula Genral", command=s_formula)
b_formula.pack()

b_newton = Button(f_menu, text="Newton Rapthson", command=s_newton)
b_newton.pack()

b_signos = Button(f_menu, text="Ley de Signos", command=s_signos)
b_signos.pack()

b_posibles = Button(f_menu, text="Posibles Raices", command=s_posibes)
b_posibles.pack()

b_sintetica = Button(f_menu, text="Division Sintetica", command=s_sintetica)
b_sintetica.pack()

b_binomios = Button(f_menu, text="Binomios de Newton", command=s_binomios)
b_binomios.pack()

b_pascal = Button(f_menu, text="Triangulo de Pascal", command=s_pascal)
b_pascal.pack()

b_binomios = Button(f_menu, text="Derivadas", command=s_derivadas)
b_binomios.pack()

b_limites = Button(f_menu, text="Limites", command=s_limites)
b_limites.pack()

b_areas = Button(f_menu,text="Areas", command=s_areas)
b_areas.pack()

b_balance = Button(f_menu,text="Balance", command=s_balance)
b_balance.pack()

b_rectas = Button(f_menu,text="Curvas", command=s_rectas)
b_rectas.pack()

b_autor = Button(f_menu, text="Autor", command=s_autor)
b_autor.pack()

root.mainloop()
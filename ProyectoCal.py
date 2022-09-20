from cgitb import text
from tkinter import *
from PIL import ImageTk,Image
import random


root = Tk()
root.title('Proyecto Final Calculo')


#--------------------------
#MENU
#--------------------------
f_menu = LabelFrame(root,padx=20,pady=20)
f_menu.grid(row=0,column=0,padx=50, pady=10)



f_formula = LabelFrame(root, text="Formula General", padx=10, pady=10)
def s_formula():
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

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
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

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
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

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
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

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
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

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
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

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
    f_formula.grid_remove()
    f_newton.grid_remove()
    f_signos.grid_remove()
    f_posibles.grid_remove()
    f_sintetica.grid_remove()
    f_binomios.grid_remove()
    f_pascal.grid_remove()
    f_autor.grid_remove()
    f_autor1.grid_remove()

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

b_autor = Button(f_menu, text="Autor", command=s_autor)
b_autor.pack()

root.mainloop()
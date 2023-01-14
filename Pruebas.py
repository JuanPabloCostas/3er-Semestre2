class ecuacion:
    def __init__(self, constante, exponente):
        self.constante = constante
        self.exponente = exponente

ecuacion1 = ecuacion(-1,3)
ecuacion2 = ecuacion(5,1)

conjunto = [ecuacion1,ecuacion2]

sup = 1.29
inf = 0
suma = conjunto[0].constante * sup ** conjunto[0].exponente + conjunto[1].constante * sup ** conjunto[1].exponente - (conjunto[0].constante * inf ** conjunto[0].exponente + conjunto[1].constante * inf ** conjunto[1].exponente)

print(suma)


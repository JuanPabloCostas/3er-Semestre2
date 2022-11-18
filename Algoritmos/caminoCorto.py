
def encontrarCamino(tabla, goal, origin):

    if tabla[goal[0]+1][goal[1]+1] == "emp":
        tabla[goal[0]+1][goal[1]+1] = definirVecinos()
    return

def definirVecinos():
    return





tabla = [["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"],
["emp","emp","emp","emp","emp","emp","emp","emp","emp","emp"]]

goal = [0,5]

origin = [7,2]

tabla[goal[0]][goal[1]] = "goa"

tabla[origin[0]][origin[1]] = "ori"

encontrarCamino(tabla,goal,origin)
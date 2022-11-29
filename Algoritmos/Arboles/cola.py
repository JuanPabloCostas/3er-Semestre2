# Costas Rueda Juan Pablo
# Torres Hernández Andrés Guadalupe
# Chavarría Villanueva Sebastian

class Cola:
    # Crea una cola vacía
    def __init__(self):
        self.data = []

    # Devuelve el contenido de la cola
    def __repr__(self):
        return " | ".join(map(str, self.data))

    # Devuelve el número de elementos de la cola
    def __len__(self):
        return len(self.data)
    
    # Añade un elemento a la cola
    def enqueue(self, e):
        self.data.append(e)

    # Extrae un elemento de la cola
    # Se lanza una excepción si la cola está vacía
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Cola vacía')
        else:
            return self.data.pop(0)

    # Devuelve el primer elemento de la cola sin extraerlo
    # Se lanza una excepción si la cola está vacía
    def peek(self):
        if self.isEmpty():
            raise IndexError('Cola vacía')
        else:
            return self.data[0]

    # Devuelve True si la cola está vacía
    def isEmpty(self):
        return self.data == []
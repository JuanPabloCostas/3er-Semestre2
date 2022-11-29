
# Costas Rueda Juan Pablo
# Torres Hernández Andrés Guadalupe
# Chavarría Villanueva Sebastian

import cola as Q

class BinarySearchTree:
    # Nodo
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        output = self.drawTree([])
        return "\n".join(map(str, output))

    def __len__(self):
        if self == None:
            return 0
        else:
            size = 1
            if self.right:
                size += self.right.__len__()
            if self.left:
                size += self.left.__len__()
            return size

    def insert(self, value):
        if self.value:
            if value < self.value:
                # Rama izquierda
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                # Rama derecha
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def delete(self, value):
        if self == None:
            return self
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            return self
        if value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)
        return self

    def getMin(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def getMax(self):
        curr = self
        while curr.right is not None:
            curr = curr.right
        return curr.value

    def exists(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left == None:
                return False
            return self.left.exists(value)
        if self.right == None:
            return False
        return self.right.exists(value)

    def inOrder(self, output):
        # Recorrido izquierda, raíz, derecha
        if self.left is not None:
            # Izquierda
            self.left.inOrder(output)
        if self.value is not None:
            # Raíz
            output.append(self.value)
        if self.right is not None:
            # Derecha
            self.right.inOrder(output)
        return output

    def preOrder(self, output):
        # Recorrido raíz, izquierda, derecha
        if self.value is not None:
            # Raíz
            output.append(self.value)
        if self.left is not None:
            # Izquierda
            self.left.preOrder(output)
        if self.right is not None:
            # Derecha
            self.right.preOrder(output)
        return output

    def postOrder(self, output):
        # Recorrido izquierda, derecha, raíz
        if self.left is not None:
            # Izquierda
            self.left.postOrder(output)
        if self.right is not None:
            # Derecha
            self.right.postOrder(output)
        if self.value is not None:
            # Raíz
            output.append(self.value)
        return output

    def levelOrder(self, output):
        # Recorrido por niveles
        if self == None:
            return output
        # Se hace uso de una cola
        q = Q.Cola()
        q.enqueue(self)
        while not q.isEmpty():
            node = q.dequeue()
            if node is None:
                continue
            output.append(node.value)
            q.enqueue(node.left)
            q.enqueue(node.right)
        return output

    def drawTree(self, output, level=0):
        # Se recorre derecha, raíz, izquierda
        if self.right is not None:
            self.right.drawTree(output, level + 1)
        if self.value is not None:
            output.append(' ' * 4 * level + f'::{self.value}')
        if self.left is not None:
            self.left.drawTree(output, level + 1)
        return output
# Costas Rueda Juan Pablo
# Torres Hernández Andrés Guadalupe
# Chavarría Villanueva Sebastian

import binary_search_tree as BST

def testBinarySearchTree():
    bst = BST.BinarySearchTree()
    data = [2,21,9,5,18,5,12,14,18,14,2,15,1,1,15,1,19,19,15]
    print("insert:", data)
    for d in data:
        bst.insert(d)
    print("size:", len(bst))
    print("in-order:", bst.inOrder([]))
    print("pre-order:", bst.preOrder([]))
    print("post-order:", bst.postOrder([]))
    print("level-order:", bst.levelOrder([]))
    print("tree:")
    print(bst)
    print("min:", bst.getMin())
    print("max:", bst.getMax())
    print("exist 25:", bst.exists(25))
    print("exist 33:", bst.exists(33))
    data = [5, 25, 50]
    print("delete:", data)
    for d in data:
        bst.delete(d)
    print("size:", len(bst))
    print("in-order:", bst.inOrder([]))
    print("tree:")
    print(bst)


if __name__ == '__main__':
    testBinarySearchTree()
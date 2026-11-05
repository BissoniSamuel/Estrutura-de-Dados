
from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        node = Node(data)
        self.root = node

    # Percurso em ordem simétrica (In-Order)
    # left, root, right
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.simetric_traversal(node.left)

        print(node)

        if node.right:
            self.simetric_traversal(node.right)

    # Percurso em pós-ordem (Post-Order)
    # left, right, root
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node)

    # Percurso em pré-ordem (Pre-Order)
    # root, left, right
    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root

        print(node)

        if node.left:
            self.preorder_traversal(node.left)

        if node.right:
            self.preorder_traversal(node.right)

    # Percurso em nível (Level-Order / Breadth-First)
    def levelorder_traversal(self, node=None):
        if node is None:
            node = self.root

        q = Queue()
        q.put(node)

        while not q.empty():
            current = q.get()

            print(current)

            if current.left:
                q.put(current.left)

            if current.right:
                q.put(current.right)


def example_tree():
    tree = BinaryTree()

    n1 = Node('B')
    n2 = Node('A')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')

    # n1.left = n7
    n5.right = n6
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    return tree


# Execução dos percursos
if __name__ == '__main__':

    tree = example_tree()
    print("Simétrico - InOrder")
    tree.simetric_traversal()

    tree2 = example_tree()
    print("\nPós Ordem - PostOrder")
    tree2.postorder_traversal()

    tree3 = example_tree()
    print("\nPré Ordem - PreOrder")
    tree3.preorder_traversal()

    tree4 = example_tree()
    print("\nEm nível - Breadth-First")
    tree4.levelorder_traversal()

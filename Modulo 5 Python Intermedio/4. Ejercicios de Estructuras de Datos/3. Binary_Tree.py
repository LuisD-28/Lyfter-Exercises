# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# root = Node('A')
# root.left = Node('B')
# root.right = Node('C')


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def print_horizontal(self):
        self._print_horizontal(self.root, 0)

    def _print_horizontal(self, node, level):
        if node is None:
            return
        
        #hijo derecho(arriba)
        self._print_horizontal(node.right, level + 1)

        #actual node
        print('   ' * level + str(node.value))

        #hijo izquierdo(abajo)
        self._print_horizontal(node.left, level + 1)


tree = BinaryTree('A')

tree.root.left = Node('B')
tree.root.right = Node('C')

tree.root.left.left = Node('D')
tree.root.left.right = Node('E')
tree.root.right.right = Node('F')

tree.print_horizontal()

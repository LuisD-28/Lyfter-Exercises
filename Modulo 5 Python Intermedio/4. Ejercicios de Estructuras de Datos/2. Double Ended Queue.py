class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
class Queue:
    def __init__(self):
        self.left = None
        self.right = None

    def push_left(self, value):
        new_node = Node(value)

        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node

    def push_right(self, value):
        new_node = Node(value)

        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
    
    def pop_left(self):
        if self.left is None:
            return None
        
        value = self.left.value

        if self.left == self.right:
            self.left = None
            self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None

        return value
    
    def pop_right(self):
        if self.right is None:
            return None
        
        value = self.right.value

        if self.left == self.right:
            self.left = None
            self.right = None
        else:
            self.right = self.right.prev
            self.right.next = None

        return value
    
    def print_queue(self):
        current = self.left
        while current is not None:
            print(current.value)
            current = current.next


d = Queue()

d.push_left('A')
d.push_right('B')
d.push_left('C')
d.push_right('D')

d.print_queue()
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print(f'Quitamos por la izquierda: {d.pop_left()}')
print(f'Quiitamos por la derecha: {d.pop_right()}')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')


d.print_queue()



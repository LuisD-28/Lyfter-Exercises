class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        
        removed = self.top
        self.top = self.top.next
        return removed.value
    
    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next



s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.push('D')

s.print_stack()


print('Popped:', s.pop())
print('Popped:', s.pop())


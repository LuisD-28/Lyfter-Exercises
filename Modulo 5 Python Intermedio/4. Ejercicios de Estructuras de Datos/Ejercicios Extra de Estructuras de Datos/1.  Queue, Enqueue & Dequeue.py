class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None #First node
        self.rear = None #Last node
    
    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.front is None:
            return None #Empty Queue
        
        value = self.front.value


        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

        return value
    
    def print_all(self):
        current = self.front
        while current is not None:
            print(current.value)
            current = current.next


q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')

q.print_all()

print('\nDequeue the first node')
print(f'{q.dequeue()}\n')

print('Print all the nodes after dequeuing the first node')
q.print_all()

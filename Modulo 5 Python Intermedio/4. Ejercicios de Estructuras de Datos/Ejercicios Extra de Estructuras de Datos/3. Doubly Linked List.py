class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None: #Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.tail is None: #Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def delete(self, data):
        if self.head is None:
            return  # Empty list

        current = self.head

        
        while current is not None and current.value != data:
            current = current.next

        if current is None:
            return  # Node not found

        
        if current == self.head:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None  # List became empty
            return

        # Case: delete tail
        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
            return

        # Case: node in the middle
        current.prev.next = current.next
        current.next.prev = current.prev

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev

dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")
print('All the nodes after appending')
dll.print_forward()
print('All the nodes in reverse order')
dll.print_backward()

dll.prepend("X")
print('\nAll the nodes after prepending')
dll.print_forward()
print('All the nodes in reverse order')
dll.print_backward()

dll.delete("B")
print('All the nodes after deleting node "B"')
dll.print_forward()
print('All the nodes in reverse order')
dll.print_backward()
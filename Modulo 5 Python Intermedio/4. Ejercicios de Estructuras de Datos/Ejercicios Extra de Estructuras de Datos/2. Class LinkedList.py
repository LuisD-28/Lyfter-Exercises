class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)

        if self.head is None: #Empty list
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self, data):
        if self.head is None:
            return #Empty list
        
        #If the node to delete is the head
        if self.head.value == data:
            self.head = self.head.next
            return

        #Search for the node to delete
        current = self.head
        while current.next is not None and current.next.value != data:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


list = LinkedList()

list.insert_front(10)
list.insert_front(20)

list.insert_back(30)

print('all the nodes after inserting')
list.print_all()

list.delete(10)

print('all the nodes after deleting 10')
list.print_all()

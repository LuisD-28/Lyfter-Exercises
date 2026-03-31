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
    
    #Validation method
    def validate_numeric(self):
        if self.left is None:
            raise ValueError("Queue is empty")
        
        current = self.left
        while current is not None:
            if not isinstance(current.value, (int, float)):
                raise ValueError("Queue contains non-numeric values")
            current = current.next

    def bubble_sort(self):
        self.validate_numeric()

        if self.left is None or self.left.next is None:
            return 0, 0
        
        passes = 0
        swaps = 0

        swapped = True
        while swapped:
            swapped = False
            passes += 1

            current = self.left
            while current.next is not None:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swaps += 1
                    swapped = True
                current = current.next

        return passes, swaps

d = Queue()

d.push_left(5)
d.push_right(3)
d.push_left('Hola')
d.push_right(1)
try:
    passes, swaps = d.bubble_sort()
except ValueError as e:
    print(e)


# d = Queue()

# d.push_left(5)
# d.push_right(3)
# d.push_left(8)
# d.push_right(1)
# d.push_left(4)
# d.push_right(2)


# print('Queue before sorting:')
# d.print_queue()

# passes, swaps = d.bubble_sort()

# print('Queue after sorting:')
# d.print_queue()

# print(f'Number of passes: {passes}')
# print(f'Number of swaps: {swaps}')




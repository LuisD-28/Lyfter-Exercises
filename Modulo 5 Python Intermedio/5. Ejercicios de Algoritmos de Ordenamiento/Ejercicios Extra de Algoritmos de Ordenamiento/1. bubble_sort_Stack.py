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

    #Validation method
    def validate_numeric(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        
        current = self.top
        while current is not None:
            if not isinstance(current.value, (int, float)):
                raise ValueError("Stack contains non-numeric values")
            current = current.next

    def bubble_sort(self):
        self.validate_numeric()
        if self.top is None or self.top.next is None:
            return 0, 0
        
        passes = 0
        swaps = 0
        
        swapped = True
        while swapped:
            swapped = False
            passes += 1

            current = self.top
            while current.next is not None:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swaps += 1
                    swapped = True
                current = current.next
        
        return passes, swaps





# s = Stack()
# s.push(5)
# s.push('hola')
# s.push(3)

# try:
#     passes, swaps = s.bubble_sort()
# except ValueError as e:
#     print(e)


s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(4)
s.push(5)

print('Stack before sorting:')
s.print_stack()

passes, swaps = s.bubble_sort()

print('Stack after sorting:')
s.print_stack()
print(f'Number of passes: {passes}')
print(f'Number of swaps: {swaps}')







class Stack:
    def __init__(self):
        self.items = []

    def _is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self._is_empty():
            raise IndexError("Empty stack")
        return self.items.pop()
    
    def peek(self):
        if self._is_empty():
            raise IndexError("Empty stack")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

# In python list are stacks
stack = []
stack.append(3) #push
stack.pop() #pop

# But...
stack = Stack()
stack.push(4)
stack.push(5)
stack.pop()
print(stack.peek())
print(stack.size())
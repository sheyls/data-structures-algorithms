from utils import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def _is_empty(self):
        return self.count == 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    
    def dequeue(self):
        if self._is_empty():
            return IndexError("Empty queue")
        
        new_head = self.head.next
        if not new_head:
            self.tail = None
        
        value = self.head.value
        self.head = new_head

        self.count -= 1
        return value

queue = Queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(5)
print(queue.dequeue())
from utils import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end= " -> ")
            current = current.next
        print("end")

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

print([my_list.head.next for _ in range(5)])

a = None
if not a:
    print("empty")

my_list.print_list()
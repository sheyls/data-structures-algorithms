from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def get(self, index: int) -> int:
        print("count", self.count)
        if index < 0 or index > self.count - 1:
            return -1
        current = self.head
        count = index
        while count > 0:
            current = current.next
            count -= 1
        return current.value

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = self.tail = Node(val)
            print("head", self.head.value)
        else: 
            current_head = self.head
            self.head = Node(val)
            self.head.next = current_head
        print("head", self.head.value)
        self.count += 1
        

    def insertTail(self, val: int) -> None:
        if not self.tail:
            self.head = self.tail = Node(val)
        else: 
            new_tail = Node(val)
            self.tail.next = new_tail
            self.tail = new_tail
        print("tail", self.tail.value)
        self.count += 1
        
    def remove(self, index: int) -> bool:
        if index < 0 or index > self.count - 1:
            return False
        
        if index == 0:
            self.head = self.head.next
            self.count -= 1
            if self.head is None:  
                self.tail = None
            return True
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
            print("current", current.value)
        
        removed_node = current.next
        current.next = removed_node.next
        
        if removed_node == self.tail:
            self.tail = current
            
        self.count -= 1
        return True

        
    def getValues(self) -> List[int]:
        items = []
        current = self.head
        while current:
            items.append(current.value)
            print("value", current.value)
            current = current.next
        return items

my_list = LinkedList()

["insertTail", 1, "insertTail", 2, "get", 1, "remove", 1, "insertTail", 2, "get", 1, "get", 0]

my_list.insertTail(1)
my_list.insertTail(2)
print(my_list.getValues())

print(my_list.get(1))
print(my_list.getValues())

print(my_list.remove(1))
print(my_list.getValues())

my_list.insertTail(2)
my_list.insertTail(3)
print(my_list.getValues())
print(my_list.get(1))
print(my_list.get(0))
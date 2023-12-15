class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.head is None
    def addFirst(self, data):
        newnode = Node(data)
        self.size += 1
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def addLast(self, data):
        newnode = Node(data)
        self.size += 1
        if self.head == None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    def addBefore(self,target, data):
        current = self.head
        newnode = Node(data)
        if self.head.data == target:
            newnode.next = self.head
            self.head = newnode
            return
        prev = None
        while current.data != target:
            if current.next == None:
                print("Target not found")
                return
            prev = current
            current = current.next
        prev.next = newnode
        newnode.next = current
        self.size += 1
    def addAfter(self, target, data):
        newnode = Node(data)
        current = self.head
        self.size += 1
        while current.data != target:
            if current.next == None:
                print("Target not found")
                return
            
            current = current.next
        newnode.next = current.next
        current.next = newnode
        
    def delete(self, key):
        current = self.head
        if current.data == key:
            self.head = current.next
            current.next = None
            self.size -= 1
            return
        while current.data != key:
            if current.next == None:
                print("key not found to delete")
                return
            prev = current
            current = current.next
        prev.next = current.next
        self.size -= 1
    def display(self):
        if self.head == None:
            print("LL is empty")
            return
        current = self.head
        while current:
            print(current.data, "->", end="")
            current = current.next
        print(None)
sll = LinkedList()
print(sll.isEmpty())
sll.addFirst(2)
sll.addFirst(1)
sll.addLast(3)
sll.display()
sll.addBefore(3, 100)
sll.addBefore(100, 10000)
sll.addBefore(1, -100)
sll.addAfter(-100, 222)
sll.display()
print(sll.size)
sll.delete(10000)
sll.delete(1)
sll.delete(3)
sll.display()
print(sll.size)

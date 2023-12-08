class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
 
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insert_after(self, prev_node, data):
        if not prev_node:
            raise ValueError("Previous node cannot be None.")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        if prev_node == self.tail:
            self.tail = new_node

    def delete(self, node):
        if self.is_empty():
            raise ValueError("List is empty.")

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.tail.next = self.head
        elif node == self.tail:
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            prev.next = self.head
            self.tail = prev
        else:
            prev = self.head
            while prev.next != node:
                prev = prev.next
            prev.next = node.next

    def display(self):

        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        print("List: ", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("NULL")

cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.prepend(0)
cll.insert_after(cll.head.next, 4)
cll.display()

cll.delete(cll.head.next)
cll.display()

cll.delete(cll.tail)
cll.display()

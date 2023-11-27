class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
    def insert_before(self, target, data):
      if self.head is None:
          print("Target not found")
          return
      if self.head.data == target:
          new_node = Node(data)
          new_node.next = self.head
          self.head = new_node
          return
      prev = None
      temp = self.head
      while temp:
          if temp.data == target:
              new_node = Node(data)
              new_node.next = temp
              prev.next = new_node
              return
          prev = temp
          temp = temp.next
      print("Target not found")
    def insert_after(self, target, data):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("Target not found")
    def display(self):
      current = self.head
      while current:
          print(current.data, "->", end=' ')
          current = current.next
      print(None)
ll = LinkedList()
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.display()
ll.insert_after(2,4)
ll.display()
ll.insert_before(4,3)
ll.display()
ll.insert_at_end(5)
ll.display()
ll.insert_at_end(6)
ll.display()
ll.delete_node(5)
ll.display()
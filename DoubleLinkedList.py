class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after(self, target, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def insert_before_node(self, target_node_data, new_data):
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == target_node_data:
                if current.prev is None:
                    new_node.next = current
                    current.prev = new_node
                    self.head = new_node
                else:
                    new_node.prev = current.prev
                    new_node.next = current
                    current.prev.next = new_node
                    current.prev = new_node
                return
            current = current.next

    def delete(self, target):
        current = self.head
        while current:
            if current.data == target:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    # Create a new doubly linked list
dll = DoublyLinkedList()

# Insert nodes at the beginning
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)

# Insert nodes at the end
dll.insert_at_end(4)
dll.insert_at_end(5)

# Insert nodes after a given node
dll.insert_after(3, 6)

# Insert nodes before a given node
dll.insert_before_node(4, 7)

# Delete a node
dll.delete(2)

# Display the list
dll.display()  # Output: 1 -> 3 -> 6 -> 4 -> 7 -> 5 -> None
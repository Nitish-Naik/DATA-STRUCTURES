class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def addLast(self, data):
        newNode = Node(data)
        currNode = self.head
        if(currNode.next == None):
            self.addFirst(data)
            return
        else:
            while(currNode.next != None):
                currNode = currNode.next
            currNode.next = newNode
            newNode.next = None
    def addBefore(self, target, data):
        currNode = self.head
        if(target == currNode.data):
            self.addFirst(data)
            return
        else:
            newNode = Node(data)
            while(currNode.data != target):
                if(currNode.next == None):
                    print("target not found")
                    return
                prevNode = currNode
                currNode = currNode.next
            prevNode.next = newNode
            newNode.next = currNode
            
    def addAfter(self, target, data):
        newNode = Node(data)
        currNode = self.head
        while currNode.data != target:
            if(currNode.next == None):
                print("Node is not found")
                return
            currNode = currNode.next
        if currNode.next == None:
            self.addLast(data)
            return
        next = currNode.next
        currNode.next = newNode
        newNode.next = next
    def delete(self, target):
        currNode = self.head
        if currNode is None:
            print("LinkedList is empty")
            return
        while currNode.data != target:
            if currNode is None:
                print("Node is not found in LinkedList")
                return
            prevNode = currNode
            currNode = currNode.next
        prevNode.next = currNode.next
    def print_list(self):
        currNode = self.head
        while(currNode):
            print(currNode.data, "->", end="")
            currNode = currNode.next
        print(None)
ll = LinkedList()
ll.addFirst(10)
ll.addFirst(9)
ll.addFirst(8)
ll.addLast(11)
ll.print_list()
ll.addBefore(11, 15)
ll.print_list()
ll.addAfter(10, 100)
ll.print_list()
ll.delete(100)
ll.print_list()
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinked:
    def __init__(self) -> None:
        self.head = None

    def addBeg(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            
            curr.next = new_node
            new_node.prev = curr

    def addPos(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            position = 0
            curr = self.head
            while curr.next and position < pos - 1:
                curr = curr.next
                position += 1
            
            new_node.next = curr.next
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node
            new_node.prev = curr

    def delBeg(self):
        if self.head is None:
            print("List Empty")
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def delEnd(self):
        if self.head is None:
            print("List Empty")
        elif self.head.next is None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
    
    def delPos(self, pos):
        if self.head is None:
            print("List Empty")
        else:
            curr = self.head
            position = 0

            while curr.next and position < pos - 1:
                curr = curr.next
                position += 1
            
            temp = curr.next
            curr.next = temp.next
            if temp.next:
                temp.next.prev = curr
    
    def displayfwd(self):
        forward = []
        curr = self.head

        while curr:
            forward.append(curr.data)
            curr = curr.next
        
        print(forward)

    def displaybwd(self):
        backward = []
        curr = self.head

        while curr and curr.next:
            curr = curr.next

        while curr: 
            backward.append(curr.data)
            curr = curr.prev
        
        print(backward)

db = DoublyLinked()

db.addBeg(10)
db.addBeg(20)
db.addBeg(30)
db.addEnd(40)
db.displayfwd()
db.delEnd()
db.addPos(15, 2)
db.displayfwd()
db.delPos(2)
db.displayfwd()

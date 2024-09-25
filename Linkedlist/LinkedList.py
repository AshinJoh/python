class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def addPos(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.addBegin(data)
            return
        
        current_pos = 0
        current = self.head

        while current and current_pos < pos - 1:
            current = current.next
            current_pos += 1
        
        new_node.next = current.next
        current.next = new_node
    
    def deleteFirst(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteLast(self):
        if self.head is None:
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def deletePos(self, pos):
        if self.head is None:
            return
        
        curr = self.head
        position = 0

        if pos == 0:
            self.deleteFirst()
        else:
            while curr and position < pos - 1:
                position += 1
                curr = curr.next
            curr.next = curr.next.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

ll = LinkedList()
ll.addBegin(10)
ll.addEnd(20)
ll.addBegin(30)
ll.addPos(40, 2)
ll.display()
ll.deletePos(2)
ll.display()

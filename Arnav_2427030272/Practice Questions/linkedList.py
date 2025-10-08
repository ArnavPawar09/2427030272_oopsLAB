class Node:
    # constructor method -> which runs automatically when new Node object created
    def __init__(self, value): # "self" -> object refers to itself
        self.value = value
        self.next = None

class LinkedList:
    # constructor method -> which runs automatically when new LinkedList created
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head == None:
            print("empty")
            return
        current = self.head
        while current is not None:
            print(current.value, end="  ")
            current = current.next
        print()

    def insert_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after_node(self, prev, data):
        if not prev:
            print("prev node not in the LL")
            return
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def delete(self, key):
        current = self.head
        if current and current.value == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.value != key:
            prev = current
            current = current.next
        if current == None:
            return
        prev.next = current.next
        current = None
        
# ---------------------------------------------

ll = LinkedList()
ll.traverse()
ll.insert_beg(1) # 1 | python interprets -> LinkedList.insert_beg(ll, 1)
ll.traverse()
ll.insert_beg(0) # 0  1
ll.traverse()
ll.insert_end(2) # 0  1  2
ll.traverse()
ll.insert_after_node(ll.head, -1) # 0  -1  1  2 
ll.traverse()
ll.delete(1) # 0  -1   2 
ll.traverse() 
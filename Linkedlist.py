class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next= new_node

    def display(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next

l1 = Linkedlist()
l1.append(4)
l1.append(6)
l1.display()
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:


    def __init__(self):
        self.head = None

    def append_data(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next = new_node
        return

    def display_data(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr=curr.next

    def give_middle(self):
        slow = self.head
        fast = self.head
        print("middle")

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
        return

l1 = Linkedlist()


l1.append_data(4)
l1.append_data(5)
l1.append_data(6)
l1.append_data(7)
l1.display_data()
l1.give_middle()

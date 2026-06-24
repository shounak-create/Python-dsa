#1. Find the length of a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_data(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        return

    def display(self):
        if self.head is None:
            return
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        return

    def list_length(self):
        if self.head is None:
            return

        curr = self.head
        count = 0
        while curr:
            count +=1
            curr=curr.next
        print(count)
        return
    #2. Reverse a linked list
    def reverselist(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        print(self.head.data)
        return
    #3. Detect a cycle (Floyd's algorithm)
    def cycle(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return

    def Merge_list(self, l1, l2):
        if l1.head is None or l2.head is None:
            return "list is empty"

        curr1 = l1.head
        curr2 = l2.head

        dummy = Node(0)
        tail = dummy

        while curr1 and curr2:
            if curr1.data < curr2.data:
                tail.next = curr1
                curr1 = curr1.next

            elif curr1.data > curr2.data:
                tail.next = curr2
                curr2 = curr2.next

            else:
                tail.next = curr1
                curr1 = curr1.next
                curr2 = curr2.next

            tail = tail.next

        if curr1:
            tail.next = curr1

        if curr2:
            tail.next = curr2

        return dummy.next


l1 = Linkedlist()
l1.insert_data(2)
l1.insert_data(3)
l1.insert_data(4)
l1.insert_data(5)
l1.insert_data(6)
# l1.display()
# l1.list_length()
print("rever")
l1.reverselist()
print(l1.cycle())

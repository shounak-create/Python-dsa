class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def merge_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next



list1 = Linkedlist()
list1.append(1)
list1.append(3)
list1.append(5)


list2 = Linkedlist()
list2.append(2)
list2.append(4)
list2.append(6)

merged = Linkedlist()
merged.head = merged.merge_lists(list1.head, list2.head)

# Display merged list
merged.display()
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def insert_data(self,root,key):

        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert_data(root.left,key)

        else:
            root.right = self.insert_data(root.right,key)

        return root


    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)


root = None

nums = [50,30,70,20,40,60,80]

l1 = BinaryTree()

for i in nums:
    root = l1.insert_data(root,i)

l1.inorder(root)
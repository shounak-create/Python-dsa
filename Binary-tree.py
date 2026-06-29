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

    def search(self,root,key):
        if root:
            if root.data == key:
                return True
            elif key < root.data:
                return self.search(root.left,key)

            elif key > root.data:
                return self.search(root.right,key)

            return False


    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def height(self,root):
        if root == None:
            return 0

        leftht = self.height(root.left)
        rightht = self.height(root.right)

        return max(leftht,rightht)+1

    def count_nodes(self,root):
        if root == None:
            return 0

        leftnd=self.count_nodes(root.left)
        rightnd=self.count_nodes(root.right)

        return leftnd+rightnd+1


root = None

nums = [50,30,70,20,40,60,80]

l1 = BinaryTree()

for i in nums:
    root = l1.insert_data(root,i)

l1.inorder(root)
print(l1.search(root,60))
print("\nheight",l1.height(root))
print("\ncount_nodes",l1.count_nodes(root))

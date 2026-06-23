class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Binarytree:
    def __init__(self):
        self.root = None

    def append_data(self,data):
        new_node = Tree(data)
        if self.head == None:
            self.head = new_node
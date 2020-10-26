class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right= right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_recur(self.root, data)
        print("*")
        return self.root

    def insert_recur(self, node, data):
        if node.data > data:
            print("L", end= '')
            if not node.left:
                node.left = Node(data)
            else:
                self.insert_recur(node.left, data)
        else:
            print("R", end='')
            if not node.right:
                node.right = Node(data)
            else:
                self.insert_recur(node.right, data)

inp = list(map(int, input("Enter Input : ").split()))
#inp = list(map(int, "1 2 5 4 3 -2 -1".split()))
bst = BST()
for x in inp:
    root = bst.insert(x)

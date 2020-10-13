class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.val:
                    if cur.left is None:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right
        return self.root

    def min(self):
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur

    def max(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur


    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print('Min :', T.min())
print('Max :', T.max())
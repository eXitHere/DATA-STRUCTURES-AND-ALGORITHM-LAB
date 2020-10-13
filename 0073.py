class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def xThree(self):
        self.val = self.val*3

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

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level+1)
            print('     '*level, node)
            self.printTree(node.left, level+1)

    def xThree(self, node, num):
        if node is not None :
            if node.val > num:
                node.xThree()
            self.xThree(node.right, num)
            self.xThree(node.left, num)


T = BST()
inp = input("Enter Input : ").split('/')
inp_num = list(map(int, inp[0].split()))
for x in inp_num:
    root = T.insert(x)
T.printTree(root)
T.xThree(root, int(inp[1]))
print('--------------------------------------------------')
T.printTree(root)
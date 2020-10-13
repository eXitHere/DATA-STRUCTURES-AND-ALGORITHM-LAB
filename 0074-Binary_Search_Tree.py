class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

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

#Preorder , Inorder , Postorder
    def preOrder(self, node):
        if node is not None:
            print(node.val, '', end='')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.val, '', end='')
            self.inOrder(node.right)

    def posOrder(self, node):
        if node is not None:
            self.posOrder(node.left)
            self.posOrder(node.right)
            print(node.val, '', end='')

    def bfs(self):
        Q = []
        Q.append(self.root)
        while len(Q) != 0:
            now = Q.pop(0)
            print(now, '', end='')
            if now.left is not None:
                Q.append(now.left)
            if now.right is not None:
                Q.append(now.right)

T = BST()
inp = input("Enter Input : ").split('/')
inp_num = list(map(int, inp[0].split()))
for x in inp_num:
    root = T.insert(x)
print("Preorder : ", end=''); T.preOrder(root); print();
print("Inorder : ", end=''); T.inOrder(root); print();
print("Postorder : ", end=''); T.posOrder(root); print();
print("Breadth : ", end=''); T.bfs(); print();
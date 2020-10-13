class Node():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left
    
    def __str__(self):
        return str(self.data)

class BST():
    def __init__(self):
        self.root = None
    
    def insertWithPostfix(self, data):
        stack = []
        for x in data:
            if x in '+-*/':
                op1 = stack.pop(-1)
                op2 = stack.pop(-1)
                stack.append(Node(x, op1, op2))
            else:
                stack.append(Node(x))
        self.root = stack.pop()
        return self.root

    def printTree(self, node, level = 0):
        if node:
            self.printTree(node.left, level+1)
            print('     ' * level, node)
            self.printTree(node.right, level+1)

    def printInfix(self, node):
        if node:
            if node.left and node.right:
                print('(', end='')
            self.printInfix(node.right)
            print(node, end='')
            self.printInfix(node.left)
            if node.left and node.right:
                print(')', end='')

    def printPrefix(self, node):
        if node:
            print(node, end='')
            self.printPrefix(node.right)
            self.printPrefix(node.left)

if __name__ == "__main__":
    T = BST()
    inp = input("Enter Postfix : ")
    root = T.insertWithPostfix(inp)
    print('Tree : ');T.printTree(root, 0)
    print('--------------------------------------------------')
    print('Infix : ',end='');T.printInfix(root);print()
    print('Prefix : ',end='');T.printPrefix(root);print()

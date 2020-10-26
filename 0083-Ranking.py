class Node:
    def __init__(self, data,rank=0,left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.lstSort = []

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def getRank(self, node):
        if node != None:
            self.getRank(node.left)
            self.lstSort.append(int(str(node)))
            self.getRank(node.right)

    def getRankStr(self):
        return self.lstSort

if __name__ == "__main__":
    inpu_ = input("Enter Input : ")
    #inpu_ = '1 2 5 4 3 -2/4'
    inp,find = list(map(int,inpu_.split('/')[0].split())),inpu_.split('/')[1]
    bst = BST()
    root = None
    for x in inp:
        root = bst.insert(root, x)
    bst.printTree(root)
    print('--------------------------------------------------')
    print("Rank of", find, ': ', end='')
    bst.getRank(root)
    lstSorted = bst.getRankStr()
    printed = False
    if int(find) < lstSorted[0]:
        print(0)
        printed = True
    else:
        for i in range(len(lstSorted)):
            if lstSorted[i] > int(find):
                print(i)
                printed = True
                break

    if not printed:
        print(len(lstSorted))
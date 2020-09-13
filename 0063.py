class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node

    def __str__(self):
        current = self.tail
        temp = []
        while current:
            temp.append(current.data)
            current = current.next
        return ' '.join(temp)

    def str_reverse(self):
        current = self.head
        temp = []
        while current:
            temp.append(current.data)
            current = current.prev
        return ' '.join(temp)

    def __add__(self, other):
        self.head.next, other.tail.prev = other.tail, self.head
        self.head = other.head
        return LinkedList(self.head, self.tail)

if __name__ == "__main__":
    lk1 = LinkedList()
    lk2 = LinkedList()
    inp = input("Enter Input (L1,L2) : ").split()
    #inp = "CE->2D Lardkrabang->KMITL".split()
    for x in inp[0].split('->'):
        lk1.append(x)
    for x in reversed(inp[1].split('->')):
        lk2.append(x)
    print("L1    :", lk1)
    print("L2    :", lk2.str_reverse())
    lk1 += lk2
    print("Merge :", lk1)
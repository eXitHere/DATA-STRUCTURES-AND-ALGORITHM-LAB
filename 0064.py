class Node:
    def __init__(self, data):
        self.data  = data
        self.next  = None

class LinkedList:
    def __init__(self):
        self.head   = None
        self.tail   = None

    def append(self,value):
        #print("org " + str(self))
        node = Node(value)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.head.next = node
            self.head = node
            self.move_cursor_after_append(node)
        

    def move_cursor_after_append(self, node):
        temp = node.data
        current = self.tail
        while current:
            if current.data == '|':
                self.swap_node(node, current)
                #self.swap_node(node, node.next)
                #current_ = current.next
                
                #while current_:
                #    self.swap_node(current_, current_.next)
                #    current_ = current_.next
                break
            current = current.next
        masterNode = self.tail
        #print(self)
        while masterNode:
            if masterNode.data == temp:
                current_ = masterNode.next
                #print(current_.data)
                while current_:
                    if(current_.data == '|'):
                        self.swap_node(current_, masterNode.next)
                        break
                    self.swap_node(current_, current.next)
                    #print("swap" + current_.data + current.next.data)
                    current_ = current_.next
            masterNode = masterNode.next
        #print()
        #print(self)

    def move_cursor_with_left(self):
        try:
            current = self.tail
            while current:
                if current.next.data == '|':
                    self.swap_node(current.next, current)
                    break
                current = current.next
        except:
            # can't move
            pass

    def move_cursor_with_right(self):
        try:
            current = self.tail
            while current:
                if current.data == '|':
                    self.swap_node(current.next, current)
                    break
                current = current.next
        except:
            # can't move
            pass
    
    def delete_back(self):
        try:
            current = self.tail
            #print(current.data)
            while current:
                if current == self.tail and current.next.data == '|':
                    self.tail = current.next
                    break
                elif current.next.next.data == '|':
                    #print("Do1")
                    current.next = current.next.next
                    break
                current = current.next
        except:
            # can't move
            pass

    def delete_d(self):
        try:
            current = self.tail
            while current:
                if current.data == '|':
                    #self.swap_node(current, current.next)
                    if current.next.next is None:
                        current.next = None
                        self.head = current
                        #print("Do 1")
                    else:
                        current.next = current.next.next
                        #print("Do 2")
                    break
                current = current.next
        except:
            # can't move
            pass

    def swap_node(self, a, b):
        try:
            a.data, b.data = b.data, a.data
        except:
            pass

    def __str__(self):
        temp = []
        current = self.tail
        while current:
            temp.append(str(current.data))
            current = current.next
        return ' '.join(temp)

if __name__ == "__main__":
    #inp = "I I,I KMITL,L,L,R,I Love".split(",")
    inp = input("Enter Input : ").split(",")
    lk = LinkedList()
    lk.append("|")
    for x in inp:
        s = x.split()
        #print(lk)
        if s[0] == 'I':
            lk.append(s[1])
        elif s[0] == 'L':
            lk.move_cursor_with_left()
        elif s[0] == 'R':
            lk.move_cursor_with_right()
        elif s[0] == 'B':
            lk.delete_back()
        elif s[0] == 'D':
            lk.delete_d()
    print(lk)
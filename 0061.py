class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def __str__(self):
        if self.isEmpty():
            return "List is empty"
        else:
            temp = "link list : "
            current = self.tail

            while current:
                temp += str(current.data) + '->'
                current = current.next
            return temp[0:-2]
    
    def append(self, data):
        node = Node(data)
        #print(node)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.head.next = node
            self.head = node
        self.count += 1
    
    def insert(self, index, data):
        node = Node(data)
        added = False
        if index == 0:
            #print("Do 1")
            if self.tail is None:
                self.tail = node
                self.head = node
            else:
                self.tail, node.next = node, self.tail
            added = True
        elif index == self.count:    
            #print("Do 2")
            self.head.next = node
            self.head = node
            added =  True
        else:
            #print("Do3")
            current = self.tail
            index_ = 0
            while current:
                index_ += 1
                if index_ == index:
                    current.next, node.next = node, current.next
                    added = True
                current = current.next
        if added:
            print("index =" , index, "and data =", data)
            self.count += 1
        else:
            print("Data cannot be added")

    def isEmpty(self):
        return self.count == 0

if __name__ == "__main__":
    #inp = "1 2, 0:0, 3:3".split(",")
    inp = input("Enter Input : ").split(",")
    lk = Linked()
    for x in inp[0].split():
        lk.append(x)
    print(lk)
    for i in range(1, len(inp)):
        split_ = inp[i].split(":")
        lk.insert(int(split_[0]), split_[1])
        print(lk)
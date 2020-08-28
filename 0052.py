class Stack:
    def __init__ (self, item=None):
        if item == None:
            self.item = []
        else:
            self.item = item

    def push(self, new_items):
        self.item.append(new_items)
        #print(self.item)
    
    def peek(self):
        return self.item[-1]
    
    def pop(self):
        temp = self.item[-1]
        self.item.pop(-1)
        return temp

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

stack = Stack()
_inp = input("Enter Input : ").split(",")
for _x in _inp:
    x,y = _x.split()
    if stack.size() and stack.peek()[0] < int(x):
        print(stack.pop()[1])
        while(stack.size() and stack.peek()[0] < int(x)):
            print(stack.pop()[1])
    stack.push((int(x), int(y)))
    

#print(stack)
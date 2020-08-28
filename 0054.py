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
#_inp = "B,B,B,A 10,A 1,A 3,A 2,B,A 1,A 1,B,A 5,A 4,B".split(",")
for x in _inp:
    if x[0] == 'A':
        _split = x.split()
        while(stack.size() and stack.peek() <= int(_split[1])):
            #print("pop", stack.pop())
            stack.pop()
        stack.push(int(_split[1]))
        #print("push", int(_split[1]))
    elif x[0] == 'B':
        print(str(stack.size()))
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

stack = Stack()
#y = "()[]"
y = input("Enter Input : ")
print("Parentheses : ", end='')
Match = True
for x in y:
    #print(x, end=' ')
    if x == '[' or x == '(' or x == '{':
        stack.push(x)
    elif x == ']':
        #print("Do1")
        if stack.size() == 0:
            Match = False
        elif stack.peek() == '[':
            stack.pop()
        else:
            Match = False
    elif x == ')':
        #print("Do2")
        if stack.size() == 0:
            Match = False
        elif stack.peek() == '(':
            stack.pop()
        else:
            Match = False
    elif x == '}':
        #print("Do3")
        if stack.size() == 0:
            Match = False
        elif stack.peek() == '{':
            stack.pop()
        else:
            Match = False

if Match and stack.size() == 0:
    print("Matched ! ! !")
else:
    print("Unmatched ! ! !")
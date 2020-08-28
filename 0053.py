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
        return str(''.join(self.item))

op = set(['+', '-', '*', '/', '(', ')', '^'])  
pr = {'+':1, '-':1, '*':2, '/':2, '^':3} 

stack = Stack()
output = ''
_inp = input("Enter Infix : ")
for x in _inp:
    if x not in op:
        output += x
    elif x =='(': 
        stack.push('(')
    elif x ==')':
        while stack.size() and stack.peek() != '(':
            output+=stack.pop()
        stack.pop()
    else:
        while stack.size() and stack.peek() != '(' and pr[x] <= pr[stack.peek()]:
            output+=stack.pop()
        stack.push(x)
while(stack.size()):
    output += stack.pop()

print("Postfix :", output)
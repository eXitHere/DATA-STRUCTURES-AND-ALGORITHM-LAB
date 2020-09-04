class Queue:
    def __init__(self, item=None):
        if item is not None:
            self.value = item
        else:
            self.value = []
        
    def peek(self):
        return self.value[0]
    
    def pop(self):
        return self.value.pop(0)

    def size(self):
        return len(self.value)

    def push(self, value):
        self.value.append(value)

    def __str__(self):
        return str(self.value)

def encodemsg(q1, q2):
    for x in range(q1.size()):
        temp = q2.pop()
        if 'A' <= q1.peek() <= 'Z':
            q1.push(str(chr(((ord(q1.pop())-ord('A')+int(temp))%26)+ord('A'))))
        elif 'a' <= q1.peek() <= 'z':
            q1.push(str(chr(((ord(q1.pop())-ord('a')+int(temp))%26)+ord('a'))))
        q2.push(temp)
    print("Encode message is : ", q1)

def decodemsg(q1, q2):
    for x in range(q1.size()):
        temp = q2.pop()
        if 'A' <= q1.peek() <= 'Z':
            q1.push(str(chr(((ord(q1.pop())-ord('A')-int(temp))%26)+ord('A'))))
        elif 'a' <= q1.peek() <= 'z':
            q1.push(str(chr(((ord(q1.pop())-ord('a')-int(temp))%26)+ord('a'))))
        q2.push(temp)
    print("Decode message is : ", q1)

inp = input("Enter String and Code : ").split(",")
q1 = Queue([x for x in inp[0] if x != ' '])
q2 = Queue([int(x) for x in inp[1]])
encodemsg(q1, q2)
q2 = Queue([int(x) for x in inp[1]])
decodemsg(q1, q2) 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


"""
1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า

4. def isEmpty(self): return list นั้นว่างหรือไม่

5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

6. def insert(self, index, data): insert data ใน index ที่กำหนด

7. def remove(self, data): remove & return node ที่มี data
"""
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        temp = "linked list : "
        current = self.tail
        while current:
            temp += str(current.data)
            if current.next:
                temp += '->'
            current = current.next
        return temp

    def str_reverse(self):
        temp = "reverse : "
        current = self.head
        while current:
            temp += str(current.data)
            if current.prev:
                temp += '->'
            current = current.prev
        return temp
    
    def isEmpty(self):
        return self.count == 0

    def append(self, data):
        node = Node(data)
        #print(self.head)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node
        self.count += 1

    def insert(self, index, data):
        #print('Debug: ', self.count)
        added = False
        node = Node(data)
        if index == 0:
            #print("Do1")
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail, node.next = node, self.tail
                node.next.prev = self.tail
            #print(self.tail.data, node.next)
            added = True
        elif index == self.count:
            #print("Do2")
            if self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.head, node.prev = node, self.head
                node.prev.next = self.head
            added = True
        else:
            #print("Do3")
            index_ = 0
            current = self.tail
            while current:
                index_ += 1
                if index == index_:
                    #print(index, index_)
                    current.next.prev, current.next, node.next, node.prev = node, node, current.next, current
                    added = True
                    break
                current = current.next
        if added:
            self.count += 1
            return "index = " + str(index) + " and data = " + str(data)
        else:
            return "Data cannot be added"

    def remove(self, data):
        current = self.tail
        index = 0
        removed = False
        while current:
            #rint("inf?")
            if current.data == data:
                print("removed :", data, "from index :", index)
                if self.count == 1:
                    self.tail = None
                    self.head = None
                elif index == 0:
                    #print("Do")
                    current.next.prev = None
                    self.tail = current.next
                elif index+1 == self.count:
                    #print("Do1")
                    current.prev.next = None
                    self.head = current.prev
                else:
                    #print("Do2")
                    current.prev.next, current.next.prev = current.next, current.prev
                self.count -=1
                removed = True
                break
            index += 1
            current = current.next
        if not removed:
            print("Not Found!")

if __name__ == "__main__":
    lk = LinkedList()
    inp = input("Enter Input : ").split(",")
    for x in inp:
        split = x.split()
        if split[0] ==  'R':
            lk.remove(split[1])
        elif split[0] == 'A':
            lk.append(split[1])    
        elif split[0] == 'I':
            s_ = split[1].split(":")
            print(lk.insert(int(s_[0]), s_[1]))
        elif split[0] == 'Ab':
            lk.insert(0, split[1])
        print(lk)
        print(lk.str_reverse())


"""
Case 5/6
Remove all member
Somethink like: --> A 1,A 6,R 6,R 5,A 7,R 1,R 7
"""
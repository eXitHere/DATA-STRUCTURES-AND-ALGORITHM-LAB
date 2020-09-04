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

inp = input("Enter Input : ").split("/")
#inp = "1 101,1 102,2 201,2 202/D,E 101,E 201,E 102,D,D,D,D".split("/")

def get_group(value_):
    for key, value in dic.items():
        if value_ in value:
            return key

def POP():
    for key,value in dic_queue.items():
        if value.size():
            return value.pop()
    return -1

dic = {}
dic_queue = {}

for x in inp[0].split(","):
    _x = x.split()
    try:
        temp = dic[int(_x[0])]
        temp.append(_x[1])
        dic[int(_x[0])] = temp
    except:
        dic[int(_x[0])] = [_x[1]]

#print(dic)

#print(dic_queue)

for x in inp[1].split(','):
    _x = x.split()
    if _x[0] == 'D':
        tempPop = POP()
        if int(tempPop) > 0:
            print(tempPop)
        else:
            print("Empty")

    elif _x[0] == 'E':
        group_id = get_group(_x[1])
        try:
            tempQ = dic_queue[group_id]
            if tempQ.size():
                tempQ.push(_x[1])
            else:
                dic_queue.pop(group_id)
                tempQ = Queue([_x[1]])
            dic_queue[group_id] = tempQ
        except:
            tempQ = Queue([_x[1]])
            dic_queue[group_id] = tempQ
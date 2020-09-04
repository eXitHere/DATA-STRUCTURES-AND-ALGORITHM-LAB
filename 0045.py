class someclass:
    def __init__(self, item=None):
        if item is not None:
            self.value = item
        else:
            self.value = []
        
    def peek(self):
        return self.value[0]
    
    def peek_back(self):
        return self.value[-1]

    def pop(self):
        return self.value.pop(0)

    def pop_back(self):
        return self.value.pop(-1)

    def size(self):
        return len(self.value)

    def push(self, value):
        self.value.append(value)

    def __str__(self):
        return str(self.value)

red, blue = input("Enter Input (Red, Blue) : ").split()
red, blue = list(red), list(blue)
#inp = "AAABBBCDDDEE BBBTENETAAA".split()

def same_three(a,b,c):
    return a == b == c

blue_counter = 0
blue_bom = someclass()
while True:
    is_break = True
    for i in range(len(blue)-2):
        if same_three(blue[i],blue[i+1],blue[i+2]):
            blue_bom.push(blue[i])
            blue.pop(i)
            blue.pop(i)
            blue.pop(i)
            blue_counter += 1
            is_break = False
            break
    if is_break:
        break
#print(blue_bom)
#print(blue)
r_counter = 0
r_m_counter = 0
while True:
    mistake  = -1
    is_break = True
    for i in range(len(red)-2):
        #print(red, red[i], red[i+1], red[i+2])
        if blue_bom.size():
            #print("boom", blue_bom.peek_back())
            if same_three(red[i],red[i+1],red[i+2]):
                red.insert(i+2, blue_bom.pop_back())
                mistake  = i
                is_break = False
                #print(mistake)
        if same_three(red[i],red[i+1],red[i+2]):
            red.pop(i)
            red.pop(i)
            red.pop(i)
            #print(i)
            if mistake == i:
                r_m_counter += 1
            else:
                r_counter += 1
            is_break = False
            break
    #print(is_break)
    if is_break:
        break

#print(red)

print("Red Team :")
print(len(red))
print(''.join(red[::-1]) if len(red) else "Empty")
print(r_counter, "Explosive(s) ! ! ! (HEAT)")
if r_m_counter:
    print("Blue Team Made (a) Mistake(s) {} Bomb(s)".format(r_m_counter))
print("----------TENETTENET----------")
print(": maeT eulB")
print(len(blue))
print(''.join(blue) if len(blue) else "ytpmE")
print("(EZEERF) ! ! ! (s)evisolpxE", blue_counter)
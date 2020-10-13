#inp = input("Enter Input : ")

def find_max(lst):
    if len(lst) == 1:
        return int(lst[0])
    else:
        m = find_max(lst[1:])
        if m > lst[0]:
            #print("returned1 ", m , lst[0])
            return m
        else:
            #print("returned2 ", lst[0])
            return lst[0]
        #return m if m > lst[0] else lst[0]



#inp = list(map(int, "8 7 10 1 5 4 2 6 3 9".split()))
#print(inp)
inp = list(map(int, input("Enter Input : ").split()))
print("Max :", find_max(inp))

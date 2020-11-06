def find_alphabet(st):
    for i in st:
        if 'a' <= i <= 'z':
            return (ord(i))
    return 0

def sort_with_alphabet(inp):
    key = []
    value = []
    for x in inp:
        key.append(find_alphabet(x))
        value.append(x)
    for i in range(len(key)):
        min_idx = i
        for j in range(i+1, len(key)):
            #print("compare ", inp[j], inp[min_idx])
            if key[j] < key[min_idx] and key[j] >= 0:
                #print("change idx", min_idx,j)
                min_idx = j
        key[min_idx], key[i] = key[i], key[min_idx]
        value[min_idx], value[i] = value[i], value[min_idx]
    return value

if __name__ == "__main__":
    inp = input("Enter Input : ").split()
    #print(inp)
    print(*sort_with_alphabet(inp))
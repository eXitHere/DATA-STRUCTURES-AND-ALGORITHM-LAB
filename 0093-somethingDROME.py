def is_min_sort(inp):
    for i in range(1, len(inp)):
        if inp[i] < inp[i-1]:
            return False
    return True

def is_max_sort(inp):
    for i in range(1, len(inp)):
        if inp[i] > inp[i-1]:
            return False
    return True

def is_duplicate(inp):
    s = set(inp)
    return not len(s) == len(inp)

if __name__ == "__main__":
    inp = list(map(int, [char for char in input("Enter Input : ")]))
    s = set(inp)
    if len(s) == 1:
        print("Repdrome")
    elif is_min_sort(inp) and is_duplicate(inp):
        print("Plaindrome")
    elif is_min_sort(inp):
        print("Metadrome")
    elif is_max_sort(inp) and is_duplicate(inp):
        print("Nialpdrome")
    elif is_max_sort(inp):
        print("Katadrome")
    else:
        print("Nondrome")
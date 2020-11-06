ans = []
bi = []
def subset(a, n, fi, s):
    if a == n:
        lst = []
        sum = 0
        for i in range(len(bi)):
            if bi[i] == 1:
                lst.append(s[i])
                sum += s[i]
        if sum == fi:
            ans.append(lst)
        return
    bi[a] = 0
    subset(a+1, n, fi, s)
    bi[a] = 1
    subset(a+1, n, fi, s)

def select_sort(inp):
    for i in range(len(inp)):
        min_idx = i
        for j in range(i+1, len(inp)):
            if inp[j] < inp[min_idx]:
                min_idx = j
        inp[min_idx], inp[i] = inp[i], inp[min_idx]
    return inp

def select_sort_with_len(inp):
    for i in range(len(inp)):
        min_idx = i
        for j in range(i+1, len(inp)):
            if len(inp[j]) < len(inp[min_idx]):
                min_idx = j
        inp[min_idx], inp[i] = inp[i], inp[min_idx]
    return inp

def select_sort_with_samelen(inp):
    for i in range(len(inp)):
        min_idx = i
        for j in range(i+1, len(inp)):
            if len(inp[j]) == len(inp[min_idx]):
                if a_more_b(inp[min_idx], inp[j]):
                    min_idx = j
        #print("min is", inp[min_idx])
        inp[min_idx], inp[i] = inp[i], inp[min_idx]
        #for x in inp:
        #    print(x)
        #print()
    return inp

def a_more_b(a,b):
    #print("compare", a, b)
    for i in range(len(a)):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    return False

if __name__ == "__main__":
    #inp_ = "2/-2 3 1 -1 0 -3 2".split("/")
    inp_ = input("Enter Input : ").split("/")
    inp = list(map(int, inp_[1].split()))
    inp = select_sort(inp)
    bi = [0]*len(inp)
    #print(inp)
    subset(0, len(inp), int(inp_[0]), inp)
    for x in (select_sort_with_samelen(select_sort_with_len(ans))):
        print(x)
    if len(ans) == 0:
        print("No Subset")
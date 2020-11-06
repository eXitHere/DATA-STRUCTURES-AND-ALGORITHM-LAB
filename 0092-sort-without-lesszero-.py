if __name__ == "__main__":
    inp = list(map(int, input("Enter Input : ").split()))
    for i in range(len(inp)):
        min_idx = i
        if inp[i] < 0:
            continue
        for j in range(i+1, len(inp)):
            #print("compare ", inp[j], inp[min_idx])
            if inp[j] < inp[min_idx] and inp[j] >= 0:
                #print("change idx", min_idx,j)
                min_idx = j
        inp[min_idx], inp[i] = inp[i], inp[min_idx]
    print(*inp)
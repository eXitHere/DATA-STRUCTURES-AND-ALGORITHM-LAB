if __name__ == "__main__":
    #inp_ = "6 2 4 3 7/3".split("/")
    inp_ = input("Enter Input : ").split("/")
    inp = list(map(int, inp_[0].split()))
    ans = 37
    max_ = sum(inp)
    min_ = max(inp)
    while min_ <= max_:
        mid = (max_ - min_) // 2 + min_
        i = 0
        c = 0
        while i < len(inp):
            w = 0
            while i < len(inp) and w + inp[i] <= mid:
                w += inp[i]
                i += 1
            c += 1
        if c <= int(inp_[1]):
            max_ = mid - 1
        else:
            min_ = mid + 1
    print("Minimum weigth for", inp_[1], "box(es) =", min_)
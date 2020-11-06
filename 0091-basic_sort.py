if __name__ == "__main__":
    inp = list(map(int, input("Enter Input : ").split()))
    #inp = list(map(int, "5252 -5 2630 -558".split()))
    for i in range(1, len(inp)):
        #print(inp[i-1], inp[i])
        if inp[i-1] > inp[i]:
            print("No")
            break
    else:
        print("Yes")
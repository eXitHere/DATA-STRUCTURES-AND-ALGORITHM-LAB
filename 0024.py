def move(n,A,B,C):
    if n > 0:
        move(n-1,A,C,B)
        print("move",n,"from ", A , "to", C)
        move(n-1,B,A,C)

move(int(input("Enter Input : ")),"A","B","C")
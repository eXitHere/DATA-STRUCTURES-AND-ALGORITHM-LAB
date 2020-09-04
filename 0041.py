inp = input("Enter Input : ").split(",")

Q = []

for x in inp:
    _x = x.split()
    if _x[0] == 'E':
        Q.append(_x[1])
        print(len(Q))
    else:
        if len(Q):
            print(Q.pop(0), 0)
        else:
            print(-1)

if len(Q):
    print(' '.join(Q))
else:
    print("Empty")
print("*** Fun with Drawing ***")
m = int(input("Enter input : "))
# 5 * 4 -3
n = (m*4-3)
pos = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i==j and i%2==0:
            for k in range(j,n-i):
                pos[i][k] = True
                pos[k][i] = True
            pos[i][n-1] = True
            for l in range(j,n-i):
                pos[k][l] = True
                pos[l][k] = True
            break

for x in range(len(pos)):
    for y in range(len(pos)):
        print('#' if pos[x][y] else '.', end='')
    print()
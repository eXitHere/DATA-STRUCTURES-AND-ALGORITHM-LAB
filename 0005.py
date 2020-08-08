n = int(input("Enter Input : "))

for i in range(2+n):
    print('.'*(2+n-i-1) + '#'*(i+1) + '+' + ('#' if i>0 and i<n+1 else '+')*(n) + '+')

for i in range(2+n):
    print('#' + ('+' if i>0 and i<n+1 else '#')*(n) + '#' + '+'*(2+n-i) + '.'*(i))
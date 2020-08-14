def odd_even(arr, s):
    if s == 'Odd':
        key = 0
    else:
        key = 1
    return ([arr[i] for i in range(len(arr)) if i%2 == key])

lst = input("*** Odd Even ***\nEnter Input : ").split(',')
if lst[0] == 'L': #string case
    if len(lst[1].split()) > 0:
        print(odd_even(lst[1].split(), lst[2]))
    else:
        print([])
elif lst[0] == 'S': #list case
    if len(lst[1].split()) > 0 :
        print(''.join(odd_even(lst[1], lst[2])))
    else:
        print([])
    

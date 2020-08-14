def removeDupli(value):
        return ''.join(sorted(set(value), key=value.index))

input_ = input("Enter String : ")
ans = []
org = removeDupli(input_)
for x in input_:
    for i in range(len(org)):
        if org[i] == x:
            ans.append(i)
            break

print(ans)
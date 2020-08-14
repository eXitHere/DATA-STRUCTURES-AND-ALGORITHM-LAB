arr = list(map(int, input("Enter Your List : ").split()))
ans = []
if len(arr) < 3:
    print("Array Input Length Must More Than 2")
else:
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(i+j+1, len(arr)):
                if (arr[i] + arr [j] + arr[k]) == 0:
                    ans.append([arr[i], arr[j], arr[k]])

    print(ans)
                 
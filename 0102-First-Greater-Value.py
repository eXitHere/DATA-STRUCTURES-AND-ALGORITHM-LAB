if __name__ == "__main__":
    inp = input('Enter Input : ').split('/')
    arr, arr2 = sorted(list(map(int, inp[0].split()))), list(
        map(int, inp[1].split()))
    #print(arr)
    for x in arr2:
        try:
            print(min(y for y in arr if y > x))
        except:
            print("No First Greater Value")

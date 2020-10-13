def palindrome(str_):
    if len(str_)<=2:
        return True
    elif str_[0] != str_[-1]:
        return False
    else:
        return palindrome(str_[1:-1])

    #print("'" + str_ + "' is palindrome")


inp = input("Enter Input : ")
print("'"+inp+"' is palindrome" if palindrome(inp) else "'"+inp+"' is not palindrome")
class funString:
    def __init__(self, myString):
        self.value = myString

    def getLen(self):
        return len(self.value)

    def switch_char(self):
        return ''.join([chr(ord(x)+32) if 'A' <= x <= 'Z' else chr(ord(x)-32) for x in self.value])

    def myReverse(self):
        return self.value[::-1]

    def removeDupli(self):
        return ''.join(sorted(set(self.value), key=self.value.index))

input_str, choice = input("Enter String and Number of Function : ").split()
xx = funString(input_str)
if int(choice) == 1:
    print(xx.getLen())
elif int(choice) == 2:
    print(xx.switch_char())
elif int(choice) == 3:
    print(xx.myReverse())
elif int(choice) == 4:
    print(xx.removeDupli())
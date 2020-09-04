inp = input("Enter Input : ").split(",")

Q_ES = []
Q_EN = []

for x in inp:
    _x = x.split()
    if _x[0] == 'EN':
        Q_EN.append(_x[1])
    elif _x[0] == 'ES':
        Q_ES.append(_x[1])
    else:
        if len(Q_ES):
            print(Q_ES.pop(0))
        elif len(Q_EN):
            print(Q_EN.pop(0))
        else:
            print("Empty")

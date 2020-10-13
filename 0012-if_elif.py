print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))
print("Wind classification is ",end = '')
if x >= 209:
    print("Super Typhoon.")
elif x >= 102:
    print("Typhoon.")
elif x >= 56:
    print("Tropical Storm.")
elif x >= 52:
    print("Depression.")
else:
    print("Breeze.")

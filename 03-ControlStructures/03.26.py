x = 0
z = 0
while x != 3:
    y = str(input("Enter Pin"))
    if y == "0805":
        print("Correct PIN")
        x = 3
        z = 1
    else:
        print("Incorrect...")
        x = x+1
if z == 1:
    print("Welcome to your Account")
else:
    print("Your card has been blocked")
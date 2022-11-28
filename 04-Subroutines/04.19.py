def check():
    a = int(input("Number: "))
    b = int(input("Range from: "))
    c = int(input("Range to: "))
    d = 0
    for i in range(b,c):
        if a == i:
            print("The number is in range")
            d = 1
    if d == 0:
        print("The number is not in range")

check()

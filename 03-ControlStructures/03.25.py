x = int(input("a: "))
y = int(input("b: "))
print("X"*x)
if y >= 2:
    for i in range(0,(y-2)):
        if x > 1:
            print("X"," "*(x-4),"X")
        if x == 1:
            print("X")
if y > 1:
    print("X"*x)
def liczby():
    print("1 2 3\n4 5 6\n7 8 9")
liczby()

print()

def liczby1():
    for x in range(1 , 10):
        print(x, end=" ")
        if x % 3 == 0:
            print("")
liczby1()
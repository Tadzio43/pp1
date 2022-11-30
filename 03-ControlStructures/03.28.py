for x in range (1,49):
    if x == 1:
        a1 = 0
        a2 = 1
        print("0")
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print(a3)
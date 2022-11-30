for x in range(1,31):
    print(x)
    if x%3 == 0 and x%5 == 0:
        print("BINGO")
    else:    
        if x%3 == 0:
            print("THREE")
        if x%5 == 0:
            print("FIVE")
def suma():
    x = int(input("X: "))
    y = int(input("Y: "))
    
    i = x
    sum = 0
    for i in range(x,y):
        sum = sum + i
    sum = sum + i + 1
    print(sum)

suma()
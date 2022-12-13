def median(x):
    print(x)
    z = len(x)
    for j in range(0,z):
        for i in range(0,z):
            if i == z-1:
                break
            if x[i] > x[i+1]:
                y = x[i]
                x[i] = x[i+1]
                x[i+1] = y
    print(x)
    if x[0] > x[-1]:
        print(x[0] - x[-1])
    else:
        print(x[int(z/2)])

y = [5,4,3,2,1]
median(y)

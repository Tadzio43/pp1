def subcheck(x,y):
    count = 0
    z = len(y)
    for i in x:
        if i in y:
            count = count + 1
    if count == len(y):
        print("Yes")
    else:
        print("No")
a = [1,2,3,4,5]
b = [1,2,3,4,5]
subcheck(a,b)
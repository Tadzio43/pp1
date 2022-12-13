a = [-15,8,-31,47,-2,19,40000,20,-129,1,2,3,4,5,6,7,8,9,10,0]
def oddeven(x):
    for i in x:
        if i%2 == 0:
            print(i," ", end="")
    print()
    for i in x:
        if i%2 != 0:
            print(i," ", end="")
oddeven(a)
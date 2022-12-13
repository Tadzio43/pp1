a = [-15,8,-31,47,-2,19,40000,20,-129,1,2,3,4,5,6,7,8,9,10,0]
def string(x):
    print(x)
    print("[", end="")
    for i in x:
        print(str(i),",", end="")
    print("]", end="")
string(a)
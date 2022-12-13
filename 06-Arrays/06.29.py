def median(x,y):
    count = 0
    for i in x:
        if y < i:
            count = count + 1
    print(count)
            
        

a = [5,4,3,2,1]
b = int(input("Podaj liczbe"))
median(a,b)

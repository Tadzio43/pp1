x = [12, 6, 4, 9, 10]
def star(n):
    stringg = ""
    n0 = n
    while n != 0:
        stringg = stringg + "*"
        n = n -1
    print(n0,":",stringg)
    return(stringg)
for i in x:
    star(i)
    
    
    
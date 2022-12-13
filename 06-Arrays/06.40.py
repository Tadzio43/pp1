x = [[-38, 19],[5,40],[-7,11],[29,16],[-38, 19],[5,40],[-7,11],[29,50],[-38, 19],[5,40],[-7,11],[29,16],[-38, 19],[5,40],[-700,11],[29,50]]
y = len(x)
m = 0
l = 0
k = 0
for i in range(0,y):
    z = len(x[i])
    j = 0
    if i == 0:
        
        if x[i][j] > x[i][j+1]:
            m = x[i][j]
            l = i
            k = 0
            print("Bigger number: ",m,"[",l,"]","[",k,"]")
        if x[i][j+1] > m:
            m = x[i][j+1]
            l = i
            k = 1
            print("Bigger number: ",m,"[",l,"]","[",k,"]")
    else:
        if x[i][j] > m:
            m = x[i][j]
            l = i
            k = 0
            print("Bigger number: ",m,"[",l,"]","[",k,"]")
        if x[i][j+1] > m:
            m = x[i][j+1]
            l = i
            k = 1
            print("Bigger number: ",m,"[",l,"]","[",k,"]")
print()
print()
print()
print()
print()
m = 0
l = 0
k = 0
for i in range(0,y):
    z = len(x[i])
    j = 0
    if i == 0:
        
        if x[i][j] < x[i][j+1]:
            m = x[i][j]
            l = i
            k = 0
            print("Smallest number: ",m,"[",l,"]","[",k,"]")
        if x[i][j+1] < m:
            m = x[i][j+1]
            l = i
            k = 1
            print("Smallest number: ",m,"[",l,"]","[",k,"]")
    else:
        if x[i][j] < m:
            m = x[i][j]
            l = i
            k = 0
            print("Smallest number: ",m,"[",l,"]","[",k,"]")
        if x[i][j+1] < m:
            m = x[i][j+1]
            l = i
            k = 1
            print("Smallest number: ",m,"[",l,"]","[",k,"]")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
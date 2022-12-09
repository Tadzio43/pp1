x = [[True,False],[True,True],[False,False]]
for i in range(0,3):
    for j in range(0,2):
        if x[i][j] == True:
            x[i][j] = False
        else:
            if x[i][j] == False:
                x[i][j] = True
print(x)
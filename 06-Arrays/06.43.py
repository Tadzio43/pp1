x = []
b = 30
for j in range(0,b):
        x.append([0]*b)
        x[j][j] = 1
for i in x:
    print(i)
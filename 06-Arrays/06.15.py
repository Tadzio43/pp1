x = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        x[i][i] = 1
print(x[0])
print(x[1])
print(x[2])
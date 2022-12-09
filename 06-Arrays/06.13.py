x = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum = 0
for i in x:
    for j in i:
        print(j," ", end="")
        if j%2 == 0:
            sum = sum + j
print()
print(sum)
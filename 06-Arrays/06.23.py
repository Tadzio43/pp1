x = [-15,8,-31,47,-2,19,40000,20,-129,1,2,3,4,5,6,7,8,9,10,0]
print(x)
z = len(x)
for j in range(0,z):
    for i in range(0,z):
        if i == z-1:
            break
        if x[i] > x[i+1]:
            y = x[i]
            x[i] = x[i+1]
            x[i+1] = y
print(x)

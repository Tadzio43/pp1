x = [-15,8,-31,47,-2,19]
print(x)
z = len(x)
print(z)
for j in range(0,z):
    for i in range(0,z):
        if i == 5:
            break
        print(x[i])
        print(x[i+1])
        if x[i] > x[i+1]:
            y = x[i]
            x[i] = x[i+1]
            x[i+1] = y
print(x)
print(x[-1])
print(x[0])

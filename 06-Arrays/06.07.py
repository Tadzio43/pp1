x = [1,2,3,4,5]
print(x)
x[0] = x[0] - 1
print(x)
x[-1] = x[-1] + 4
print(x)
x[int(len(x)/2)] = x[int(len(x)/2)]*2
print(x)
for i in range(0,len(x)):
    x[i] = x[i] + 3
print(x)
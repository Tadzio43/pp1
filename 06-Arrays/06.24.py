x = [2,3,2,5,8,1,9,8,2,3,4,5,0,2,5,3,1,2,3,5,4,3,3,2,3,123452,5,6,7,8,9,8,7,6,2341234,5,4,2,4,2,34,3,4]
z = len(x)
y = [0]*z
j = 0
for i in x:
    if i in y:
        continue
    else:
        y[j] = i
        j = j + 1
m = 1
while m != 0:
    if 0 in y:
        y.remove(0)
    else:
        m = 0
print(y)

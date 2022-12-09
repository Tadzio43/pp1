x = [2,3,7,5,4]
print(x)
print(len(x))
print(x[0])
print(x[1])
print(x[-1])
print(x[-2])
print(x[0]+x[-1])
print(x[int(len(x)/2)])
for i in x:
    print(i," ", end="")
print()
for i in x:
    print(i," ", end="")
    if i == 7:
        break


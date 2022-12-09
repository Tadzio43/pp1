x = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
y = [0,0,0,0,0]
for i in range(0,5):
    for j in x[i]:
        y[i] = y[i] + 1
print(x[y.index(max(y))])
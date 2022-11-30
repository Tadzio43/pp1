i = 1
e = -1
x = [0]*100
suma = 0
count = 0
while i != 0:
    e = e + 1
    y = int(input("Enter number: "))
    x[e] = y
    if x[e] == 0:
        i = 0
for a in x:
    suma = suma + a
    if a > 0:
        count = count + 1

print("Suma liczb ",suma)
print("Ilość wprowadzonych liczb ",count)
print("Średnia artmetyczna wprowadzych liczb ",suma/count)
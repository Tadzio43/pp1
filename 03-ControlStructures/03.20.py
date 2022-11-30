x = int(input("Enter a number for multiplication table: "))
y = int(input("Enter how many multiplications you want (starting from times one): "))
y = y+1
for i in range(1,y):
    print(x," * ",i," = ",x*i)
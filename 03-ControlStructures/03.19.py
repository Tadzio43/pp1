x = int(input("Enter the dog's age in human years: "))
if x > 2:
    x = x -2
    age = (2*10.5)+(x*4)
else:
    age = (x*10.5)
age = int(age)    
print("The dog's age in dog's years is: ",age)

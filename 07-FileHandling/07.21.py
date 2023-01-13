import random

file = open("MeatAndFish.txt","w")
for x in range(0,10):
    file.write(str(x+1))
    file.write(" ")
    file.write(str((x+1)*(x+1)))
    file.write(" ")
    file.write(str((x+1)*(x+1)*(x+1)))
    file.write("\n")
file.close()
file = open("MeatAndFish.txt","r")
for line in file:
    print(line)
file.close()

    
    
    
    
    
    
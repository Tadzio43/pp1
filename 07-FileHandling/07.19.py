file = open("MeatAndFish.txt","w")
for x in range(0,50):
    file.write(str(x+1))
    file.write("\n")
file.close()
file = open("MeatAndFish.txt","r")
for line in file:
    print(line)
file.close()

    
    
    
    
    
    
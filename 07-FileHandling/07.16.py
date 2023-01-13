file = open("filmy.txt","w")
x = ["shrek","shrek2","shrek3","shrek4","shrek5","shrek","shrek2","shrek3","shrek4","shrek5","shrek","shrek2","shrek3","shrek4","shrek5","shrek","shrek2","shrek3","shrek4","shrek5","shrek","shrek2","shrek3","shrek4","shrek5","shrek","shrek2","shrek3","shrek4","shrek5555555555",]
for i in x:
    file.write(i)
    file.write("\n")
file.close()
file = open("filmy.txt","r")
count = 0
for line in file:
    count = count + 1
print("Number of lines: ",count)
file.close()
file = open("filmy.txt","r")
limit = 0
z = []
for line in file:
    print(line)
    z.append(line)
    limit = limit + 1
    if limit == 5:
        y = input("Press enter to continue")
file.close()
file = open("copy.txt","w")
for j in z:
    file.write(j)
    file.write("\n")
file.close()
file = open("copy.txt","r")
for line in file:
    print(line)
file.close()
    
    
    
    
    
    
    
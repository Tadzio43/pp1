file = open("filmy.txt","w")
x = ["shrek","shrek2","shrek3","shrek4","shrek5"]
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
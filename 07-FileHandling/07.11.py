file = open("filmy.txt","w")
x = ["shrek","shrek2","shrek3","shrek4","shrek5"]
for i in x:
    file.write(i)
    file.write("\n")
file.close()
file = open("filmy.txt","r")
file_content = file.read()
print( file_content )
file.close()
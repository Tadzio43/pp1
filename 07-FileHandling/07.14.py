x = ["apple \n","banana \n","egg \n","milk \n","onion \n"]
file = open("filmy.txt","w")
for i in x:
    file.write(i)
file.close()
o = str(input("Podaj nazwe pliku "))
filename = open(o,"r")
count = 0
for line in filename:
    count = count + 1
print("Number of lines: ",count)
file.close()
    

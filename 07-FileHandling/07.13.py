x = ["apple \n","banana \n","egg \n","milk \n","onion \n"]
file = open("filmy.txt","w")
for i in x:
    file.write(i)
file.close()
file = open("filmy.txt","r")
file_content = file.read()
print( file_content )
file.close()
file = open("filmy.txt","a")
y = str(input("dodaj produkt: "))
file.write(y)
file.close()
file = open("filmy.txt","r")
file_content = file.read()
print( file_content )
file.close()
with open("filmy.txt") as file:
   fl = file.read()
   for line in fl:
       print(line)

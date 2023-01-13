file = open("MeatAndFish.txt","w")
x = ["Skinless white meat","Tuna fish","Luncheon meat","Lean cuts of red meat"]
for i in x:
    file.write(i)
    file.write("\n")
file.close()
file = open("MeatAndFish.txt","r")
for line in file:
    print(line)
file.close()
file = open("GrainsAndBread.txt","w")
v = ["Bread","Rice","All purpose flour","Breakfast cereal","Pasta"]
for k in v:
    file.write(k)
    file.write("\n")
file.close()
file = open("GrainsAndBread.txt","r")
for line in file:
    print(line)
file.close()
z = []
file = open("MeatAndFish.txt","r")
limit = 0
for line in file:
    z.append(line)
    limit = limit + 1
file.close()
file = open("GrainsAndBread.txt","r")
limit = 0
for line in file:
    z.append(line)
    limit = limit + 1
file.close()
file = open("shoppinglist.txt","w")
for j in z:
    file.write(j)
    file.write("\n")
file.close()
file = open("shoppinglist.txt","r")
print("------------------------")
for line in file:
    print(line)
file.close()
    
    
    
    
    
    
    
import csv

file = open("MeatAndFish.txt","w")
file.write("first_name,last_name,age,gender,email\n")
file.write("Decca,Blackstone,52,Male,dblackstone0@time.com\n")
file.write("Elena,Rechert,27,Female,erechert1@ucoz.com\n")
file.write("Bibbye,Norree,26,Female,bnorree2@reddit.com\n")
file.write("Alasdair,McCoole,53,Male,amccoole3@foxnews.com\n")
file.write("Hogan,Hatrey,26,Male,hhatrey4@zimbio.com\n")
file.close()
rows = []
file = open("MeatAndFish.txt","r")
csvreader = csv.reader(file)
fields = next(csvreader)
for row in csvreader:
    if int(row[2]) < 30:
            print("  ".join([row[0],row[1],row[4]]))
            print()
file.close()

    
    
    
    
    
    
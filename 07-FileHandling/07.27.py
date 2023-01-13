import re

file = open("Grades.txt","w")
file.write("Name: Peter\n")
file.write("Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0\n")
file.close()
file = open("Grades.txt","r")
file_content = file.read()
message = file_content
pattern = "\d+\.*\d+"
ugabuga = re.findall(pattern,message)
suma = 0
licznik = 0
for x in ugabuga:
    z = float(x)
    suma = suma + z
    licznik = licznik + 1
    wynik = suma/licznik
print(float(wynik))
file.close()
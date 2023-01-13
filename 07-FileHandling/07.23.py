import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
pattern = r"(\w+)C"
temperatures = re.findall(pattern,message)
print(temperatures)
y = 0
count = 0
for x in temperatures:
    z = int(x)
    y = y + z
    count = count + 1
y = y/count
print("Średnia temperatur to: ",y)
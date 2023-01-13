import re

message = "To be, or not to be, that is the question"
patterns = ["a","e","i","o","u","y"]
suma = 0
for pattern in patterns:
    ugabuga = re.findall(pattern,message)
    suma = suma+len(ugabuga)
print(suma)
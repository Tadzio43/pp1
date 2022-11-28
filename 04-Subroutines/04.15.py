import random

def read_number():
    x = int(input("Enter number: "))
    return x
def generate_number():
    y = random.randrange(1,9)
    print(y)
    return y
    
x = read_number()
y = generate_number()
if y == x:
    print("You won the game!")
else:
        print("You lost the game!")
def bigger_smaller():
    x = int(input("X: "))
    y = int(input("Y: "))
    z = True
    if y >= x:
        z = False
    return z

print(bigger_smaller())

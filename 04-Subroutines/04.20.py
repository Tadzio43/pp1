def power(x,n):
    powerx = x*(x*(n-1))
    if powerx == 0:
        powerx = 1
    return powerx

print(power(5,2))

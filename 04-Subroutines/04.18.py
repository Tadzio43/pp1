def sum_digit(digit):
    sum = 0
    y = str(digit)
    for i in y:
        x = int(i)
        sum = sum + x
    return sum
    
print(sum_digit(7182))
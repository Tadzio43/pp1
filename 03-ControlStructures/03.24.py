y = 2
for x in range(1,10):
    if x <= 5:
        print("* "*x)
    if x > 5:
        print("* "*(x-y))
        y = y+2
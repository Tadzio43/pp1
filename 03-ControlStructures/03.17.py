x = int(input("First part of coordinates: "))
y = int(input("Second part of coordinates: "))
if x > 0 and y > 0:
    print("Point (",x,",",y,") is in the first quadrant of the coordinate system")
else: 
    if x < 0 and y > 0:
        print("Point (",x,",",y,") is in the second quadrant of the coordinate system")
    else:
        if x < 0 and y < 0:
            print("Point (",x,",",y,") is in the third quadrant of the coordinate system")
        else:
            if x > 0 and y < 0:
                print("Point (",x,",",y,") is in the fourth quadrant of the coordinate system")
            else:
                if x == 0 and y == 0:
                    print("Point (",x,",",y,") is in the the middle of the coordinate system")
                else:
                    if x == 0 and y < 0:
                        print("Point (",x,",",y,") is in between the third and the fourth quadrant of the coordinate system")
                    else:
                        if x == 0 and y > 0:
                            print("Point (",x,",",y,") is in between the first and the second quadrant of the coordinate system")
                        else:
                            if x < 0 and y == 0:
                                print("Point (",x,",",y,") is in between the second and the third quadrant of the coordinate system")
                            else: 
                                if x > 0 and y == 0:
                                    print("Point (",x,",",y,") is in between the first and the fourth quadrant of the coordinate system")
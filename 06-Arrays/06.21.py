def compare(array1,array2):
    if len(array1) == len(array2):
        i = len(array1)-1
        l = 1
        while i != 0:
            if array1[i] == array2[i]:
                i = i - 1
            else:
                print("These arrays are diffrent")
                l = 0
                break
    else:
        print("These arrays are diffrent")
        l = 0
    if l == 1:
        print("These arrays are the same")
        
x = [3,2,1]
y = [3,2,1]
compare(x,y)
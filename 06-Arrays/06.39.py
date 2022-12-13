number_of_rows = 5
number_of_columns = 5
arr_2d=[]
for x in range(number_of_rows):
   column_elements=[]
   for y in range(number_of_columns):
       column_elements.append(0)
   arr_2d.append(column_elements)
print(arr_2d)
n = 0
p = 0
o = 1
for i in arr_2d:
    for j in i:
        if o == 1:
            g = 1
        if o == 2:
            g = 2
        if o == 3:
            g = 3
        if o == 4:
            g = 4
        if o == 5:
            g = 5
        i[0+p] = (1 + n)*g
        p = p + 1
        n = n + 1
    p = 0
    n = 0
    o = o + 1
    print(i)
        
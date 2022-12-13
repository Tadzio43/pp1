number_of_rows = 3
number_of_columns = 5
arr_2d=[]
for x in range(number_of_rows):
   column_elements=[]
   for y in range(number_of_columns):
       column_elements.append(0)
   arr_2d.append(column_elements)
print(arr_2d)
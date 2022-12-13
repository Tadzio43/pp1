from random import *

def rand_elem(n):
    createList = []
    for i in range(1,n+1):
        createList.append(i)
    x = randint(1,n+1)
    print(createList[x])

rand_elem(999)
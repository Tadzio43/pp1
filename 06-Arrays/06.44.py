def b():
    x = [[1,2,3,4,5],[6,7,8,9,0]]
    for a in x:
        print(a)
    print()
    result = [[1,2],[3,4],[5,6],[7,8],[9,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[j][i] = x[i][j]
    for r in result:
        print(r)
def a():
    x = [[1,2,3],[4,5,6],[7,8,9]]
    for a in x:
        print(a)
    print()
    result = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[j][i] = x[i][j]
    for r in result:
        print(r)
def c():
    x = [5,6,7,8]
    for a in x:
        print(a)
    print()
    result = [[5],[6],[7],[8]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[j][i] = x[i][j]
    for r in result:
        print(r)
c()
        
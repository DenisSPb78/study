x = int(input()) #размерность квадратной матрицы
sp = [[1 for i in range(x)] for j in range(x)]
for i in range(x):
    for j in range(x):
        if (i>j and i<(x-1-j)) or (i<j and (i<x-1-j)) or (i/2<x/2 and j/2<x/2 and (i+ j)+1<x):
            sp[i][j] = 0
        elif (i<j and i>(x-1-j)) or (i>j and (i<x-1-j)) or (i/2<x/2 and j/2<x/2 and (i+ j)+1>x):
            sp[i][j] = 2
    print(*sp[i])
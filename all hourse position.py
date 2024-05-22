sp = [['.' for i in range(8)] for i in range(8)]
hor = input() # f5
res = ['a','b','c','d','e','f','g','h','i']
x, y = 8-int(hor[1]), res.index(hor[0])
sp[x][y] = 'H'
for i in range(8):
    for j in range(8):
        if abs((x - i) * (y - j)) == 2:
            sp[i][j] = '*'
    print(*sp[i])
n, m = 5, 5  #Можно ввести через map(int, input().split())  '3 6'
sp = [[0] *m for j in range(n)]
d_row = 0
d_col = -1
i = 1
x, y = 0, -1

while i <= n*m:
    if 0<= x+ d_row < n and 0<= y+d_col<m and sp[x+d_row][y+d_col] ==0:
        x+=d_row
        y+=d_col
        sp[x][y] = i
        i+=1
    else:
        if d_col==1:
            d_col = 0
            d_row = 1
        elif d_row == 1:
            d_col = -1
            d_row = 0
        elif d_col == -1:
            d_col = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_col = 1
for i in sp:
    print(*i)
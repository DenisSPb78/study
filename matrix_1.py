x = 1
m,n = map(int, input().split())
sp = [[0 for i in range(n)] for j in range(m)]
for i in range(len(sp)):
    for j in range(len(sp[i])):
        sp[i][j] = x
        x+=1
    print(*sp[i])
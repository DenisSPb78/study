import math

#рисуем треугольник Паскаля по заданному количеству уровней
def fac(n):
    res = 1
    for i in range(1, n+1):
        res*=i
    return res

n = int(input())+1  #Задаём количество отрисовываемых уровней
sp = []
for j in range(1, n):
    sp = []
    for i in range(1, j-1):
        sp.append(math.ceil(fac(j-1)/(fac(i)*(fac(j-1-i)))))

    if j == 1:
        sp.append(1)
    else:
        sp.insert(0, 1)
        sp.append(1)
    print(*sp)

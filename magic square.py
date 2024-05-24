sp = [list(map(int, input().split())) for _ in range(int(input()))]
#  3 размер квадрата
#8 1 6
#3 5 7
#4 9 2
res = True
s_v = [] #делаем плоский список для понимания - одинаковые цифры внутри квадрата или нет
v_p = [[] for i in range(len(sp[0]))] #собираем сумму по столбцам
horiz = [] # собираем суммы строк и диагоналей
a, b = 0, 0
for j in range(len(sp)):
    a += sp[j][j]
    b += sp[len(sp) - j - 1][j]
horiz.append(a)
horiz.append(b)
for i in range(len(sp)):
    horiz.append(sum(sp[i]))
    z = 0
    for j in range(len(sp[i])):
        s_v.append(sp[i][j])
        z+=sp[j][i]
    v_p[i] = z

if len(set(s_v)) == 1 or len(set(v_p)) > 1 or 0 in s_v or len(set(s_v)) != len(s_v) or len(set(horiz)) != 1:
    res = False

print('YES' if res else 'NO')
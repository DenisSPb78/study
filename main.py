#На вход программе подается строка текста, содержащая символы. Программу упаковывает последовательности одинаковых символов заданной строки в подсписки
#'w w w o r l d g g g g r e a t t e c c h e m g g p w w'
x = input().split()
sp = [[x[0]]]
for i in range(1, len(x)):

    if x[i] in sp[-1]:
        sp[-1].append(x[i])
    else:
        sp.append([x[i]])
print(sp)
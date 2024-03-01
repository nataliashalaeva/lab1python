# Задание 9 Прочитать список строк с клавиатуры. Упорядочить по длине строки.
l = []
s = input()
l.append(s)
while s != "": 
    s = input()
    if (s != ""): l.append(s)
print(sorted(l, key=len))

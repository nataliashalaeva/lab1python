# Задание 9 Прочитать список строк с клавиатуры. Упорядочить по длине строки.

strings = []
print("Введите строки :")
while True:
    string = input()
    if string == "":
        break
    strings.append(string)

print("Отсортированный список строк по длине:")
print(*sorted(strings, key=len), sep=" ")

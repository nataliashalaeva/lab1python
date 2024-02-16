#Задачи 2,10,17
#2 Дана строка, состоящая из символов латиницы. Необходимо проверить, упорядочены ли строчные символы этой строки по возрастанию.
def check(string):
    chars = [char for char in string if char.islower()]
    for i in range(1, len(chars)):
        if chars[i] < chars[i-1]:
            return False
    return True
#10 Дана строка. Необходимо подсчитать количество букв "А" в этой строке.
def cou(string):
    count = 0
    for letter in string:
        if letter == 'A':
            count += 1
    return count

#17 Дана строка в которой записан путь к файлу. Необходимо найти имя файла без расширения.
def file(path):
    components = path.split('/')
    filename_with_extension = components[-1]
    filename_parts = filename_with_extension.split('.')
    filename = filename_parts[0]
    return filename

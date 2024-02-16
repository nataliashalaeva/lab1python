#Задачи 2,10,17
#2 Дана строка. Необходимо найти все строчные символы латиницы, которые в ней используются.
  
#10 Дана строка. Необходимо найти количество задействованных символов латиницы в этой строке (без дубликатов).

#17 Дана строка в которой записан путь к файлу. Необходимо найти имя файла без расширения.
def file(path):
    components = path.split('/')
    filename_with_extension = components[-1]
    filename_parts = filename_with_extension.split('.')
    filename = filename_parts[0]
    return filename

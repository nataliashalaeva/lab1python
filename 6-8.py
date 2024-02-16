#Задачи 2,10,17
#2 Дана строка. Необходимо найти все строчные символы латиницы, которые в ней используются.
  def find(string):
    letters = set()
    for char in string:
        if char.islower() and char.isalpha():
            letters.add(char)
    return letters
    
#10 Дана строка. Необходимо найти количество задействованных символов латиницы в этой строке (без дубликатов).
def cou(string):
   chars = set()
   for char in string:
       if char.isalpha() and char.isascii() and char.islower():
          chars.add(char)
  return len(chars)

#17 Дана строка в которой записан путь к файлу. Необходимо найти имя файла без расширения.
def file(path):
    components = path.split('/')
    filename_with_extension = components[-1]
    filename_parts = filename_with_extension.split('.')
    filename = filename_parts[0]
    return filename

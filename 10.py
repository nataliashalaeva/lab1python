#10 Дан список строк с клавиатуры. Упорядочить по количеству
слов в строке.

def count_words(string):
    return len(string.split())

strings = []
print("Введите строки (для завершения введите пустую строку):")
while True:
    string = input()
    if string == "":
        break
    strings.append(string)

print(sorted(strings, key=count_words))

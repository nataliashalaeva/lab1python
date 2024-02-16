#Дана строка. Необходимо найти все даты, которые описаны в виде "31 февраля 2007"
import re
def date(string):
    pat = r"\d{1,2} (?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) \d{4}"
    dates = re.findall(pat, string)
    return dates

text = input("Введите текст")
result = date(text)
print(result)

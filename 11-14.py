Вариант 2 
# Функция для сортировки строк в порядке увеличения среднего веса ASCII-кода символов
def sort_by_avg_ascii(strings):
    return sorted(strings, key=lambda x: sum(ord(c) for c in x) / len(x))
  
#4 4 В порядке увеличения квадратичного отклонения среднего веса ASCII-кода символа строки от среднего веса ASCII-кода символа первой строки.

#7 В порядке увеличения разницы между количеством сочетаний «гласная-согласная» и «согласная-гласная» в строке.
#11 В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке.


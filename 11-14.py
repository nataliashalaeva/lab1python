Вариант 2 
# Функция для сортировки строк в порядке увеличения среднего веса ASCII-кода символов
def sort_by_avg_ascii(strings):
    return sorted(strings, key=lambda x: sum(ord(c) for c in x) / len(x))
  
#4 4 В порядке увеличения квадратичного отклонения среднего веса ASCII-кода символа строки от среднего веса ASCII-кода символа первой строки.
def sort_by_quad_deviation(strings):
    first_string_avg = sum(ord(c) for c in strings[0]) / len(strings[0])
    return sorted(strings, key=lambda x: (sum((ord(c) - first_string_avg) ** 2 for c in x) / len(x)) ** 0.5)
    
#7 В порядке увеличения разницы между количеством сочетаний «гласная-согласная» и «согласная-гласная» в строке.
def count_vowel_consonant_combinations(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_consonant_count = 0
    consonant_vowel_count = 0
    for i in range(len(string) - 1):
        if string[i] in vowels and string[i+1] in consonants:
            vowel_consonant_count += 1
        elif string[i] in consonants and string[i+1] in vowels:
            consonant_vowel_count += 1
    return abs(vowel_consonant_count - consonant_vowel_count)
#11 В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке.


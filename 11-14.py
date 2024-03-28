Вариант 2 
# Функция для сортировки строк в порядке увеличения среднего веса ASCII-кода символов
def sort_by_avg_ascii(strings):
    return sorted(strings, key=lambda x: sum(ord(c) for c in x) / len(x))
  
#4 4 В порядке увеличения квадратичного отклонения среднего веса ASCII-кода символа строки от среднего веса ASCII-кода символа первой строки.
def sort_by_quad_deviation(strings):
    first_string_avg = sum(ord(c) for c in strings[0]) / len(strings[0]) # среднее значение ASCII кодов символов в первой строке из списка
    return sorted(strings, key=lambda x: (sum((ord(c) - first_string_avg) ** 2 for c in x) / len(x)) ** 0.5) # в каждой строки x, вычисляется квадратичное отклонение от среднего значения ASCII кодов первой строки first_string_avg. Затем строки сортируются в порядке возрастания этого отклонения.
    
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
def sort_by_vowel_consonant_combinations(strings):
    return sorted(strings, key=count_vowel_consonant_combinations)

#11 В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке.
# Функция для вычисления среднего веса ASCII-кода тройки символов в строке
def avg_ascii_weight_triple(string):
    triple_weights = [sum(ord(c) for c in string[i:i+3]) / 3 for i in range(len(string) - 2)]
    return max(triple_weights) if triple_weights else 0
    
# Функция для вычисления квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке
def quadratic_deviation(strings):
    if len(strings) < 2:
        return 0
    first_string_avg = avg_ascii_weight_triple(strings[0])
    max_avg = max(avg_ascii_weight_triple(string) for string in strings[1:])
    return (max_avg - first_string_avg) ** 2
    
def quadratic_deviation_sort(strings):
     return sorted(strings, key=quadratic_deviation)

if __name__ == "__main__":
    strings = []
    print("Введите строки:")
    while True:
        string = input()
        if string == "":
            break
        strings.append(string)

    choice = input("Выберите задачу (1, 2, 3, 4): ")

    if choice == "1":
        sorted_strings = sort_by_avg_ascii(strings)
    elif choice == "2":
        sorted_strings = sort_by_quad_deviation(strings)
    elif choice == "3":
        sorted_strings = sort_by_vowel_consonant_combinations(strings)
    elif choice =="4":
        sorted_strings = quadratic_deviation_sort(strings)
    else:
        print("Некорректный выбор задачи.")
        exit()

    print("Отсортированный список строк:")
    for string in sorted_strings:
        print(string)



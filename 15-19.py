#2 Дан целочисленный массив. Необходимо найти индекс минимального элемента.
def func1(l):
    return l.index(min(l))
  
#14 Дан целочисленный массив и интервал a..b. Необходимо найти количество элементов в этом интервале.
def func2(l, a, b):
    k = 0
    for i in l:
        if i > a and i < b:
            k += 1
    return k
  
#26 Дан целочисленный массив. Необходимо найти количество элементов между первым и последним минимальным.
def func3(l):
    minEl = min(l)
    first = -1
    last = -1
    for i in range(0,len(l)):
        if l[i] == minEl:
            if first == -1: first = i
            else: last = i
    k = 0
    for i in range(0,len(l)):
        if i > first and i < last: k += 1
    return k
  
#38 Дан целочисленный массив и отрезок a..b. Необходимо найти количество элементов, значение которых принадлежит этому отрезку.

def func4(l, a, b):
    k = 0
    for i in l:
        if i >= a and i <= b:
            k += 1
    return k
  
#50 Для двух введенных списков L1 и L2 построить новый список, состоящий из элементов, встречающихся только в одном из этих списков и не повторяющихся в них.
def func5(l1, l2):
    l = []
    for i in l1:
        if i not in l2 and l1.count(i) == 1: l.append(i)
    for i in l2:
        if i not in l1 and l2.count(i) == 1: l.append(i)
    return l



#10 Дан список строк с клавиатуры. Упорядочить по количеству
слов в строке.
def f(string):
    return len(string.split(" "))

l = []
s = input()
l.append(s)
while s != "": 
    s = input()
    if (s != ""): l.append(s)
print(sorted(l, key=f))

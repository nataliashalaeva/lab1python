#1 Найти количество чисел, взаимно простых с заданным.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cou(n):
    count = 0
    for i in range(1, n+1):
        if gcd(n, i) == 1:
            count += 1
    return count

#2 Найти сумму цифр числа, делящихся на 3
def fun2(n):
   sum=0
   while n>0:
     k=n%10
     if k%3 ==0:
        sum+=k
     n=n//10
   return sum

#3 Найти делитель числа, являющийся взаимно простым с суммой цифр данного числа
def fun3(n):
  sum=0
  w=n
  while n>0:
    k=n%10
    sum+=k
    n=n//10
  for i in range(2, w):
    if w%i==0:
        gcd(sum, i) == 1
        break
  return i

n =int(input())
print(cou(n))
print(fun2(n))
print(fun3(n))

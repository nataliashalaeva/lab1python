#1 задача
import math
def fun1(n):
   k=0
   for i in range(1, n+1):
      if math.gcd(n, i) == 1:
       k+=1
   return k

#2 задача
def fun2(n):
   sum=0
   while n>0:
     k=n%10
     if k%3 ==0:
        sum+=k
     n=n//10
   return sum

#3 задача
import math
w = int(input())
sum=0
n=w
while n>0:
    k=n%10
    sum+=k
    n=n//10
for i in range(2, w):
    if w%i==0:
        math.gcd(sum, i) == 1
        break
print(i)

n =int(input())
print(fun1(n))
print(fun2(n))
print(fun3(n))

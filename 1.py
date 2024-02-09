#1 задача
import math
w = int(input())
k=0
for i in range(1, w+1):
    if math.gcd(w, i) == 1:
       k+=1
print(k)

#2 задача
n=int(input())
sum=0
while n>0:
    k=n%10
    print(k)
    if k%3 ==0:
        sum+=k
    n=n//10
print(sum)

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



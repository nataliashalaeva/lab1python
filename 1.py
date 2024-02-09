# диапазон [1,100]
import math
w = int(input())
k=0
for i in range(1, n+1):
    if math.gcd(w, i) == 1:
       k+=1
print(k)


n=int(input())
sum=0
while n>0:
    k=n%10
    print(k)
    if k%3 ==0:
        sum+=k
    n=n//10
print(sum)



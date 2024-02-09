# диапазон [1,100]
import math
start = 1
end = 100
w = int(input())
k=0
for i in range(start, end+1):
    if math.gcd(w, i) == 1:
       k+=1
print(k)



from math import floor,sqrt
n=int(raw_input())
p=int(floor(sqrt(n)))
sum=0
for i in range(1,p+1):
    sum+=floor(n/i) - (i-1)
print int(sum)
# your code goes here
def get(n):
    sum=0
    while n>0:
        sum+=(n%10)**2
        n=n/10
    return sum
def check(n):
    count=1
    n=int(n)
    l=[]
    sum=get(n)
    l.append(sum)
    while sum!=1:
        sum=get(sum)
        if sum in l:
            return -1
        l.append(sum)
        count+=1
    return count
n=int(raw_input())
print check(n)
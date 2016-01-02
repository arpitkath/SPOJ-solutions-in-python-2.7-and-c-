# your code goes here
def z(n):
    count=0
    i=5
    m=int(n/5)
    while m>0:
        count+=m
        i*=5
        m=int(n/i)
    return count
n=int(raw_input())
for i in range(n):
    n=int(raw_input())
    print z(n)
        
# your code goes here
def f(n):
    c=0
    while n>1:
        n=n/2
        c+=1
    return c
        
n=int(raw_input())
c=0
while n!=0:
    print f(n)
    n=int(raw_input())

from math import ceil
def o(n):
    a=0.00
    for i in range(2,n+2):
        k=1.0/i
        a+=k
    a=ceil(a*100)/100.0
    return a
def f(c):
    n=0
    while True:
        if c>=(o(n)):
            n+=1
        else:
            return n
n=float(raw_input())
while n!=0:
    print str(f(n))+" card(s)"
    n=float(raw_input())
    
# cook your code here
from fractions import gcd
def f(a,b):
    return (a*b)/(gcd(a,b)**2)
a,b=map(int,raw_input().split())
while a!=0 and b!=0:
    print f(a,b)
    a,b=map(int,raw_input().split())

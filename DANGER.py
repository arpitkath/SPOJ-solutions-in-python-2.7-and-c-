# your code goes here
# cook your code here
from math import floor,log
def f(s):
    s=list(s)
    x=s[0]
    y=s[1]
    z=int(s[3])
    n=int(x+y)
    n=n*(10**z)
    k=floor(log(n,2))
    k=2**k
    k=2*(n-k)+1
    return int(k)
s=raw_input()
while s!="00e0":
    print f(s)
    s=raw_input()
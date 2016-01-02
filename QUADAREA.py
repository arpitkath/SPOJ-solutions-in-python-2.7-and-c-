from math import sqrt
def brah(s):
    s=s.split()
    a=float(s[0])
    b=float(s[1])
    c=float(s[2])
    d=float(s[3])
    s=(a+b+c+d)/2.0
    av=sqrt((s-a)*(s-b)*(s-c)*(s-d))
    return av
t=int(raw_input())
for i in range(t):
    s=raw_input()
    print brah(s)
    
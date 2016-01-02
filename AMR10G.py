#from math import mod
def f():
    nk=raw_input()
    nk=nk.split()
    n=int(nk[0])
    k=int(nk[1])
    s=raw_input()
    s=s.split()
    s=map(int,s)
    s.sort()
    l=[]
    if n==k:
        return s[n-1]-s[0]
    if k==0 or k==1:
        return 0
    for i in range(n-k+1):
        d=abs(s[i]-s[i+k-1])
        l.append(d)
    l.sort()
    return l[0]
t=int(raw_input())
for i in range(t):
    print f()
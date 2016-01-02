from math import sqrt
def fact(n):
    l=[]
    dict={}
    k=2
    while n%k==0:
        if k not in l:
            l.append(k)
            dict[str(k)]=1
            n=n/k
        else:
            dict[str(k)]+=1
            n/=k
    t=int(sqrt(n))
    for k in range(3,t+1,2):
        while n%k==0:
            if k not in l:
                l.append(k)
                dict[str(k)]=1
                n=n/k
            else:
                dict[str(k)]+=1
                n/=k
    if n>1:
        if n not in l:
            dict[str(n)]=1
        else:
            dict[str(n)]+=1
    return dict
def f(s):
    s=s.split()
    s=map(int,s)
    a=s[0]
    b=s[1]
    ad=fact(a)
    bd=fact(b)
    for key in ad.keys():
        if key in bd.keys():
            if ad[key]>=bd[key]:
                ad[key]-=bd[key]
                bd[key]=0
            else:
                bd[key]-=ad[key]
                ad[key]=0
    x=1
    y=1
    for key in ad.keys():
        y*=int(key)**ad[key]
    for key in bd.keys():
        x*=int(key)**bd[key]
    return str(x)+" "+str(y)
t=int(raw_input())
for i in range(t):
    s=raw_input()
    print f(s)+"\n"
    
        
        
    
def hero():
    s=raw_input()
    s=s.split()
    n=int(s[0])
    m=int(s[1])
    d=int(s[2])
    h=[]
    for i in range(n):
        k=int(raw_input())
        h.append(k)
    h.sort(reverse=True)
    k=0
    temp=0
    tot=d*m
    while tot!=0:
        #if k<n:
        if h[k]-d>0:
            h[k]-=d
            temp+=1
            tot-=d
        else:
            if k==n-1:
                return "NO"
            k+=1
        #else:
            #break
    if temp==m:
        return "YES"
    else:
        return "NO"
t=int(raw_input())
for i in range(t):
    print hero()
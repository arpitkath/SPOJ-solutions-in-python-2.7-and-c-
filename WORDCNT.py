def f(s):
    s=s.split()
    l=[]
    l2=[0]
    count=0
    max=0
    for i in s:
        l.append(len(i))
    for i in range(1,len(l)):
        if l[i-1]==l[i]:
            continue
        else:
            l2.append(i)
    l2.append(len(l))
    for i in range(len(l2)):
        count=l2[i]-l2[i-1]
        if count>=max:
            max=count
    
    if count==0 and max==0:
        return len(s)
        
    if count>=max:
        return count
    return max
t=int(raw_input())
for i in range(t):
    s=raw_input()
    print f(s)
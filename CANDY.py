def cand(n):
    l=[]
    sum=0
    ans=0
    for i in range(n):
        k=int(raw_input())
        l.append(k)
        sum+=k
    avg=int(sum/n)
    if avg*n!=sum:
        return -1
    for i in l:
        if i>avg:
            ans+=abs(avg-i)
    return ans
t=int(raw_input())
while t!=-1:
    #n=int(raw_input())
    print cand(t)
    t=int(raw_input())
        
    
    
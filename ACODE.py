def f(n):
    dp=[1]*2+[0]*100000
    l=map(int,list(str(n)))
    for i in range(2,len(l)+1):
        prev,curr=l[i-2],l[i-1]
        if prev==1 or (prev==2 and curr<=6):
            dp[i]=dp[i-2]
        if curr!=0:
            dp[i]+=dp[i-1]
    return dp[len(l)]
t=int(raw_input())
while t!=0:
    print f(t)
    t=int(raw_input())

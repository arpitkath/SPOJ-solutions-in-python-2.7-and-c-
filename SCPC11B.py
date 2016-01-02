def f(n):
    l=[]
    for i in range(n):
        l.append(int(raw_input()))
    l.sort()
    diff=[]
    if (1422-l[-1])>100:
        return "IMPOSSIBLE"
    for i in range(1,n):
        diff.append(l[i]-l[i-1])
    for  i in diff:
        if i>200:
            return 'IMPOSSIBLE'
    return "POSSIBLE"
n=int(raw_input())
while n!=0:
    print f(n)
    n=int(raw_input())
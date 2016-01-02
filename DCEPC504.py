def f(n):
    if n==1:
        return "Male"
    if n==2:
        return "Female"
    n-=1
    ones=0
    while n>1:
        if n%2==1:
            ones+=1
        n=n>>1
    if ones%2==0:
        return "Female"
    return "Male"
t=int(raw_input())
for i in range(t):
    n,k=map(int,raw_input().split())
    print f(k)
# your code goes here
def f(n):
    ans=0.0
    k=n
    for i in range(n):
        ans+=n/(k*1.0)
        k-=1
    print ("%.2f")%(ans)
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    f(n)
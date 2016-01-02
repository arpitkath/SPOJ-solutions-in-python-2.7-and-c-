def f():
    k=raw_input()
    n=int(raw_input())
    sum=0
    e=n
    while e!=0:
        t=int(raw_input())
        sum=(sum+t)%n
        e-=1
    if sum==0:
        return "YES"
    else:
        return "NO"
t=int(raw_input())
for i in range(t):
    print f()


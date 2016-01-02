def f(n):
    a=192
    d=250
    k=a+((n-1)*d)
    return k
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    print f(n)
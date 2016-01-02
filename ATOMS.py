from math import log
def f(n,k,m):
    if n>=m:
        return 0
    t=int(log(m/n)/log(k))
    return t
t=int(raw_input())
for i in range(t):
    n,k,m=map(int ,raw_input().split())
    print f(n,k,m)
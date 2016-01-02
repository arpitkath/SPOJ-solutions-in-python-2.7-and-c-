def a(n):
    return (n*(n+1)+(n-1)*(n)/2)%1000007
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    print a(n)

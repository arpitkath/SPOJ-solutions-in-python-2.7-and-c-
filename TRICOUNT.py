# your code goes here
def t(n):
    if n%2==0:
        return (n*(n+2)*(2*n+1))/8
    else:
        return (n*(n+2)*(2*n+1)-1)/8
k=int(raw_input())
for i in range(k):
    n=int(raw_input())
    print t(n)
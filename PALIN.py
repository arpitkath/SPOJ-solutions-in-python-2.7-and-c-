def isp(s):
    s=str(s)
    rev=s[::-1]
    if s==rev:
        return True
    else:
        return False
def f(n):
    i=n+1
    while True:
        if isp(i):
            return i
        else:
            i+=1
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    print f(n)
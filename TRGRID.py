# cook your code here
def f(s):
    s=s.split()
    s=map(int,s)
    n=s[0]
    m=s[1]
    if n==m or m>n:
        if n%2==0:
            return "L"
        else:
            return "R"
    else :
        if m%2==0:
            return "U"
        else:
            return "D"
t=int(raw_input())
for i in range(t):
    s=raw_input()
    print f(s)
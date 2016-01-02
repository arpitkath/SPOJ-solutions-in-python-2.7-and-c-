def val(s):
    s=list(s)
    value=0
    for i in s:
        if i==".":
            value+=1
        elif i=="-":
            value+=5
        elif i=='S':
            value+=0
        else:
            continue
    return value
def f(n):
    num=0
    while n!=-1:
        s=raw_input()
        if n>=3:
            num+=val(s)*360*(20**(n-3))
        elif n==2:
            num+=val(s)*20
        elif n==1:
            num+=val(s)
        n-=1
    return num
n=int(raw_input())
while n!=0:
    print f(n)
    n=int(raw_input())

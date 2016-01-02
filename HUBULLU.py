def f(a,b):
    if b==0:
        return "Airborne wins."
    return "Pagfloyd wins."
t=int(raw_input())
for i in range(t):
    a,b=map(int,raw_input().split())
    print f(a,b)
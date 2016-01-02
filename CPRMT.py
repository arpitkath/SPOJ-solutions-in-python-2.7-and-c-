# your code goes here
def f():
    a=list(raw_input())
    b=list(raw_input())
    c=""
    if len(b)>len(a):
        a,b=b,a
    for i in a:
        if i in b:
            c+=i
            b.remove(i)
    b=sorted(c)
    return "".join(b)
while True:
    try:
        print f()
    except EOFError:
        break
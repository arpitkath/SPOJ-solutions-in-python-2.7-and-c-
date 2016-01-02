dict={}
def f(n):
    if n>=(n/2)+(n/3)+(n/4):
        return n
    elif dict.has_key(n):
        return dict[n]
    else:
        dict[n]=f(n/2)+f(n/3)+f(n/4)
        return dict[n]
while True:
    try:
        n=int(raw_input())
        print f(n)
    except EOFError:
        break
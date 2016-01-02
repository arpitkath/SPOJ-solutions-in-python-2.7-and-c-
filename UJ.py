
def f(s):
    s=s.split()
    s=map(int,s)
    n=s[0]
    d=s[1]
    print n**d
    
s=raw_input()
while s!="0 0":
    f(s)
    s=raw_input()
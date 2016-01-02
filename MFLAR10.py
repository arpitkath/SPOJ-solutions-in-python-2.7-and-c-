# your code goes here
def f(s):
    s=s.split()
    n=len(s)
    if n==1:
        return "Y"
    l=[]
    for i in s:
        l.append(i[0].lower())
    for i in l:
        if i==l[0]:
            continue
        else:
            return "N"
    return "Y"
s=raw_input()
while s!="*":
    print f(s)
    s=raw_input()
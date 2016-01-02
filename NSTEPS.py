# your code goes here
def num(s):
    s=s.split()
    x=int(s[0])
    y=int(s[1])
    if x==y or (x-y)==2 :
        if x%2==0:
            return x+y
        else:
            return x+y-1
    else:
        return "No Number"
n=int(raw_input())
for i in range(n):
    s=raw_input()
    print num(s)
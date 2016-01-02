from math import ceil
def minm(s):
    s=s.split()
    a=int(s[0])
    b=int(s[1])
    if a==0 and b==0:
    	return 0
    if a==b:
        return 1
    else:
        return int(ceil(max(a,b)/(min(a,b)+1.0)))
s=raw_input()
while s!=("-1 -1"):
    print minm(s)
    s=raw_input()
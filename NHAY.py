# cook your code here
def f(s):
    i,j=0,-1
    l=[0]*(len(s)+1)
    l[0]=-1
    while i<len(s):
        while j>=0 and s[i]!=s[j]:
            j=l[j]
        i+=1
        j+=1
        l[i]=j
    return l
def g(s,p):
    l=f(p)
    i,j=0,0
    ans=[]
    while i<len(s):
        while j>=0 and s[i]!=p[j]:
            j=l[j]
        i+=1
        j+=1
        if j==len(p):
            ans.append(i-len(p))
            j=l[j]
    return ans
while True:
    try:
    	n=raw_input()
    	p=raw_input()
    	s=raw_input()
    	l=g(s,p)
    	if len(l)==0:
        	print"\n"
    	else:
            for i in l:
                print "%d"%(i)
    except EOFError:
        break
        
def absys():
    s1=raw_input()
    s=raw_input()
    s=s.split()
    p=[]
    a,b,c=0,0,0
    for i in s:
        if not (i=='+' or i=='='):
            try:
                i=int(i)
                p.append(i)
            except:
                p.append(i)
    if type(p[0])==str:
        print str(abs(p[1]-p[2]))+" + "+str(p[1])+" = "+str(p[2])
    elif type(p[1])==str:
        print str(p[0])+" + "+str(abs(p[0]-p[2]))+" = "+str(p[2])
    elif type(p[2])==str:
        print str(p[0])+" + "+str(p[1])+" = "+str(abs(p[0]+p[1]))
t=int(raw_input())
for i in range(t):
    absys()
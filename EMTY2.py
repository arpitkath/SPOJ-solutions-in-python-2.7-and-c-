def f(s):
    stk=[]
    co=0
    c=0
    for i in s:
        if i=="1":
            c+=1
            stk.append(0)
        elif i=="0":
            if len(stk)==0:
                return False
            stk[-1]+=1
            if stk[-1]==2:
                del stk[-1]
                c-=1
    if len(stk)==0 and c==0:
        return True
    return False
t=int(raw_input())
for i in range(1,t+1):
    s=raw_input()
    if f(s):
        print "Case %d: yes"%(i)
    else:
        print "Case %d: no"%(i)
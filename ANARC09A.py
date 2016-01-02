def f(s):
    s=list(s)
    count=0
    stk=[]
    for i in range(len(s)):
        if i==0 and s[i]=="}":
            count+=1
            stk.append("{")
        elif s[i]=='{':
            stk.append(s[i])
        elif s[i]=="}":
            if len(stk)==0:
                count+=1
                stk.append("{")
            else:
                
                del stk[-1]
    if len(stk)==0:
        return count
    else:
        if len(stk)%2==0:
            count+=(len(stk))/2
        else:
            count+=(len(stk))/2+1
        return count
s=raw_input()
i=1
while "-" not in list(s):
    print "%d. %d"%(i,f(s))
    i+=1
    s=raw_input()
    
                
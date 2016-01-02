def f(n):
    dict={}
    for i in range(n):
        s=int("".join(raw_input().split()))
        if s in dict:
            dict[s]+=1
        else:
            dict[s]=1
    k=raw_input()
    #print dict
    l=dict.keys()
    l.sort()
    #print l
    for i in l:
        temp=str(i)
        count=26-len(temp)
        for j in range(count):
            temp="0"+temp
        temp=list(temp)
        temp.insert(2," ")
        temp.insert(11," ")
        temp.insert(16," ")
        temp.insert(21," ")
        temp.insert(26," ")
        temp="".join(temp)
        temp=temp+" "+str(dict[i])
        print temp
t=int(raw_input())
for i in xrange(t):
    n=int(raw_input())
    f(n)
    if i!=t-1:
        print ""
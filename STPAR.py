# cook your code here
def stpar():
    s=raw_input()
    s=s.split()
    l=map(int,s)
    s=map(int,s)
    len_s=len(s)
    temp=[]
    stk=[]
    k=1
    length=0
    while len(l)!=0:
        if l[0]==k:
            length+=1
            #stk.append(l[0])
            del l[0]
            k+=1        
        elif (len(temp)!=0 and temp[0]==k):
            length+=1
            k+=1
            del temp[0]
        else:
            temp.insert(0,l[0])
            del l[0]
         
    if (len(temp)!=0) :
        a=temp[:]
        temp.sort()

        if (temp==a):
            length+=len(temp)
        
    if length==len_s:
        print "yes"
    else:
        print "no"
t=int(raw_input())
while t!=0:
    stpar()
    t=int(raw_input())

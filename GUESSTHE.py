def f(s):
    dict={2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0}
    l=[2,3,5,7,11,13,17,19]
    for i in range(2,len(s)+1):
        temp=i
        if s[i-1]=="Y":
            #l.append(i)
            for j in l:
                count=0
                if j>i:
                    break
                while temp%j==0 and temp>0:
                    count+=1
                    temp/=j
                if count>dict[j]:
                    dict[j]=count
    #print dict
    #for i in l:
     #   k=lcm(k,i)
    #print "l=",k
    num=1
    for i in dict:
        #print i
        num=num*(i**dict[i])
        #print num
    #print num
    for i in range(1,len(s)+1):
        if s[i-1]=="N" and num%i==0:
            return -1
    return num
s=raw_input()
while s!='*':
    print f(s)
    s=raw_input()#YYYYNN
def pizza(n):
    dict={'1/4':0,'1/2':0,'3/4':0}
    for i in range(n):
        s=raw_input()
        dict[s]+=1
    np=1
    a=dict['1/4']
    b=dict['3/4']
    c=dict['1/2']
    if a>b:
        np+=b
        a=a-b
        b=0
    elif a==b:
        np+=a
        a=0
        b=0
    else:
        np+=a
        #a=0
        b=b-a
        a=0
    if c%2==0:
        np+=c/2
        c=0
    else:
        np+=c/2
        c=1
    if a==0 and b==0 and c==0:
        return np
    if a==0 and c==0 and b!=0:
        np+=b
        return np
    elif a==0 and b==0 and c!=0:
        np+=c
        return np
    elif b==0 and c==0 and a!=0:
        if a%4==0:
            np+=a/4
        else:
            np+=a/4+1
        return np
    if a==0 and b!=0 and c!=0:
        np+=b+c
        return np
    if b==0 and a!=0 and c!=0:
        if a%4==3:
            np+=a/4+c+1
        else:
            np+=a/4+c
        return np
n=int(raw_input())
print pizza(n)
        
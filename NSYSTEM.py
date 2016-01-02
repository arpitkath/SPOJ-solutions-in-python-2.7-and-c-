def sym_to_int(s):
    s=list(s)
    num=[]
    let=[]
    flag=0
    i=0
    while i<len(s):
        if flag==0:
            flag=1
            try:
                temp=int(s[i])
                num.append(temp)
                i+=1
            except ValueError:
                num.append(1)
        else:
            flag=0
            let.append(s[i])
            i+=1
    val=0
    dict={'m':1000,'c':100,'x':10,'i':1}
    for i in range(len(num)):
        val+=num[i]*dict[let[i]]
    return val
def int_to_sym(n):
    m=n/1000
    n%=1000
    c=n/100
    n%=100
    x=n/10
    i=n%10
    if m==1:
        m='m'
    elif m==0:
        m=''
    else:
        m=str(m)+'m'
    if c==1:
        c='c'
    elif c==0:
        c=''
    else:
        c=str(c)+'c'
    if x==1:
        x='x'
    elif x==0:
        x=''
    else:
        x=str(x)+'x'
    if i==1:
        i='i'
    elif i==0:
        i=''
    else:
        i=str(i)+'i'
    res=m+c+x+i
    return res
def f(s):
    s=s.split()
    a=sym_to_int(s[0])
    b=sym_to_int(s[1])
    res=int_to_sym(a+b)
    return res
t=int(raw_input())
for i in range(t):
    s=raw_input()
    print f(s)
    
def lcs(a,b):
    #a=map(int,a.split())
    b=map(int,b.split())
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                lengths[i][j]=lengths[i-1][j-1]+1
            else:
                lengths[i][j]=max(lengths[i-1][j],lengths[i][j-1])
    return lengths[len(a)][len(b)]-1
def f(s):
    s=map(int,s.split())
    s1=raw_input()
    l=[]
    while s1!="0":
        l.append(lcs(s,s1))
        s1=raw_input()
    return max(l)
t=int(raw_input())
for i in range(t):
    s=raw_input()
    print f(s)

"""while True:
    try:
        s=raw_input()
        print f(s)
    except EOFError:
        break"""
                # your code goes here
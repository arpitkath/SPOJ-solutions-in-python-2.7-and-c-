def f(n):
    tot=[]
    for t in range(n):
        s=raw_input()
        s=s.split()
        for i in range(len(s)):
            if s[i] not in tot and i!=1:
                tot.append(s[i])
    return len(tot)-n
n=int(raw_input())
print f(n)
    
    
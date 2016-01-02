def ad(s):
    s=s.split()
    a=s[0]
    d=s[1]
    if a==0 and d==0:
        return
    sa=raw_input()
    sa=sa.split()
    sd=raw_input()
    sd=sd.split()
    sa=map(int,sa)
    sd=map(int,sd)
    sa.sort()
    sd.sort()
    if sa[0]>=sd[1]:
        print "N"
    else:
        print "Y"
s=raw_input()
while s!="0 0":
    ad(s)
    s=raw_input()
    